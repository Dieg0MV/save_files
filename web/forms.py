from .models import *
from django import forms

class document(forms.ModelForm):
  class Meta():
    model = firm
    fields= '__all__'
  #curp_file = forms.FileField()
  #acta_file = forms.FileField()
  #comp_file = forms.FileField()
  