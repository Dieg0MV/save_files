from django.shortcuts import render
from .forms import document
import base64
import json
import requests

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
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

@csrf_exempt
def Firm_Digital(request):
    if request.method == "POST":
        date = json.loads(request.body)
        image_data = date.get('image')
        
        if image_data:
          image_data = image_data.split(",")[1]
        
          decode = base64.b64decode(image_data)
          image_path = 'imgn.png'
          
          with open(image_path, 'wb') as file:
            file.write(decode)
          return JsonResponse({'message': 'Imagen recibida y guardada'})   
    return render(request, 'firm.html')

            