# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .bmi import calculate_bmi
from .form import BMIForm

# Create your tests here.

class TestBMI_form(TestCase):
	def test_form_valid(self): # (testing for success)
		data_set1 = {'height': 1.55, 'weight': 77} # funkcija moze imati vise assertova
		form = BMIForm(data_set1) # bindanje form ana data_set1
		self.assertTrue(form.is_valid()) # ako je true u zagradama i assertTrue

		data_set1 = {'height': 1.55, 'weight': 77}
		form = BMIForm(data_set1) # bindanje form ana data_set1
		self.assertTrue(form.is_valid()) # ako je true u zagradama i assertTrue

		data_set1 = {'height': 1.55, 'weight': 77, 'gender': 'm'} # funkcija moze imati vise assertova
		form = BMIForm(data_set1) # bindanje form ana data_set1
		self.assertTrue(form.is_valid()) # ako je true u zagradama i assertTrue

		data_set1 = {'height': 1.55, 'weight': 77, 'gender': 'f'}
		form = BMIForm(data_set1) # bindanje form ana data_set1
		self.assertTrue(form.is_valid()) # ako je true u zagradama i assertTrue

		data_set1 = {'height': 1.55, 'weight': 77, 'gender': 'bilo sto drugo'}
		form = BMIForm(data_set1) # bindanje form ana data_set1
		self.assertFalse(form.is_valid()) # ako je true u zagradama i assertTrue

	def test_form_not_valid(self): # (testiranje za neuspjeh)
		data_set1 = {'height': 1.55} # funkcija moze imati vise assertova
		form = BMIForm(data_set1) # bindanje form ana data_set1
		self.assertFalse(form.is_valid()) # ako je true u zagradama i assertTrue

		data_set1 = {'weight': 55} 
		form = BMIForm(data_set1) 
		self.assertFalse(form.is_valid()) 

		data_set1 = {} 
		form = BMIForm(data_set1) 
		self.assertFalse(form.is_valid()) 


	def test_weight_out_of_range(self):
		data_set1 = {'height':1.77, 'weight': 46} 
		form = BMIForm(data_set1) 
		self.assertTrue(form.is_valid()) 

		data_set1 = {'height':1.77, 'weight': 45} 
		form = BMIForm(data_set1) 
		self.assertFalse(form.is_valid()) 

		data_set1 = {'height':1.77, 'weight': 200} 
		form = BMIForm(data_set1) 
		self.assertTrue(form.is_valid()) 

		data_set1 = {'height':1.77, 'weight': 201} 
		form = BMIForm(data_set1) 
		self.assertFalse(form.is_valid()) 

	def test_height_out_of_range(self):
		data_set1 = {'height':1.1, 'weight': 55} 
		form = BMIForm(data_set1) 
		self.assertTrue(form.is_valid()) 

		data_set1 = {'height':1.0, 'weight': 55} 
		form = BMIForm(data_set1) 
		self.assertFalse(form.is_valid()) 

		data_set1 = {'height':2.30, 'weight': 55} 
		form = BMIForm(data_set1) 
		self.assertTrue(form.is_valid()) 

		data_set1 = {'height':2.31, 'weight': 55} 
		form = BMIForm(data_set1) 
		self.assertFalse(form.is_valid()) 



class TestBMI_calculation(TestCase): # testing for success
	def test_calculation_correct(self):
		result = calculate_bmi(1.68, 59) # funkciji moramo pokriti roundanje da bi se u konacnici napisala takva funkcija
		self.assertEqual(result, 20.90) # iznova ce se raditi provjera za unose

	def test_weight_out_of_range(self):
		result = calculate_bmi(1.68, 45) # unjeli smo tezinu koja nije u rasponu
		self.assertEqual(result, -1.0) # zbog toga smo dogovorili

		result = calculate_bmi(1.68, 201) # unjeli smo tezinu koja nije u rasponu
		self.assertEqual(result, -1.0)

	def test_height_out_of_range(self):
		result = calculate_bmi(2.31, 59) # unjeli smo visinu koja nije u rasponu
		self.assertEqual(result, -1.0)

		result = calculate_bmi(1.0, 59) # unjeli smo visinu koja nije u rasponu
		self.assertEqual(result, -1.0)

	def test_height_weight_out_of_range(self):
		result = calculate_bmi(2.31, 201) # unjeli smo visinu i tezinu koja nije u rasponu
		self.assertEqual(result, -1.0) # zbog toga smo dogovorili da ce u tom slucaju bmi biti -1.0

	def test_null_division(self):
		result = calculate_bmi(0, 59) # dijeljenje sa '0', sto ako se posalje string..., testira se unit bez obzira na cjelinu, ne zna se tko ce pozivati funkciju pa se pokrivaju svi scenariji
		self.assertEqual(result, -1.0)




