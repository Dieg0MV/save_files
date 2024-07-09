from django.shortcuts import render
from .forms import document
# Create your views here.

def index(request):
  form = document()
  if request.method == 'POST':
    form = document(request.POST, request.FILES)
    if form.is_valid():
      form.save()
  
  return render(request, 'index.html', {'form':form})