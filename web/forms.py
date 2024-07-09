from .models import *
from django import forms

class document(forms.ModelForm):
  class Meta():
    model = firm
    fields= '__all__'

  