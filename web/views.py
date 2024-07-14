from django.shortcuts import render
from .forms import document
from django.http import HttpResponse
# Create your views here.

def index(request):
  form = document()
  if request.method == 'POST':
    form = document(request.POST, request.FILES) 
    if form.is_valid():
      form.save()
      return HttpResponse('sucess')
    else:
      print(form.errors)
      return HttpResponse('error')
  return render(request, 'index.html', {'form':form})



def Firm_Digital(request):
  
  return render(request, 'firm.html')