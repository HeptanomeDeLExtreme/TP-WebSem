
#-*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput



class NumberInput(TextInput):
    input_type = 'number'

class SearchForm(forms.Form):
        keywords = forms.CharField(max_length=100)
        jaccard_index = forms.FloatField(required=True, max_value=1, min_value=0, widget=NumberInput(attrs={'min':'0', 'max':'1', 'step': "0.01"}))
        

    
