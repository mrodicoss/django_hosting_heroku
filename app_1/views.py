# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .form import BMIForm, FormAPI
from django.views import View
from django.http import JsonResponse
import requests, json
from django.template.loader import render_to_string

# Create your views here.
def form(request):
	form = BMIForm()
	return render(request, 'form.html', {'form': form})

class Movies(View):
	form_class = FormAPI
	form_template = 'form_movie.html'
	movie_template = 'movies.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class() # initial=self.initial)
		return render(request, self.form_template, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# <process form cleaned data>8
			movie_url = 'https://theimdbapi.org/api/find/movie?title={}'.format(
				form.cleaned_data.get('title', ''))
			
			year = form.cleaned_data.get('year', False)
			if year:
				movie_url += '&year={}'.format(year)

			api_response = requests.get(movie_url)

			if api_response.status_code != 200:
				return HttpResponseBadRequest()
			return render(request, self.movie_template, {'data': json.loads(api_response.content)})
		return render(request, self.form_template, {'form': form})

class MyFormView(View): # as_view i dispatch
    form_class = BMIForm
    #initial = {'key': 'value'}
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()#initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

class MyFormView2(MyFormView):
	template_name = 'drugi.html'

class Welcome(View):
	template_name = 'welcome.html'
	
	def get(self, request):	
		return render(request, self.template_name)


class Ajax(View):
	template_name = 'ajax.html'	
	def get(self, request):
		template = render_to_string(self.template_name)
		return JsonResponse({'template': template})	
