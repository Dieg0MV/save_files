from django.shortcuts import render
from .forms import document
from django.http import HttpResponse
# Create your views here.

def index(request):
  form = document()
  if request.method == 'POST':
    print(request.FILES)
    form = document(request.POST, request.FILES) 
    if form.is_valid():
      form.save()
      return HttpResponse('sucess')
    else:
      
      return HttpResponse('error')
  return render(request, 'index.html', {'form':form})