from django import forms

class BMIForm(forms.Form):
	height = forms.FloatField(label='height', min_value=1.1, max_value=2.30,required=True)
	weight = forms.IntegerField(label='weight', min_value=46, max_value=200, required=True)
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices=[('m', 'male'),('f', 'female')], required=False)


class FormAPI(forms.Form):
	title = forms.CharField(max_length=100)
	year = forms.IntegerField(min_value=1920, max_value=2020, required=False)
