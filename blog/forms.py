from django import forms
from django.forms import ModelForm
from .models import Query

#Creating a query form

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ('name','contact','email','query')
        
