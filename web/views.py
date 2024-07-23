from django.shortcuts import render
from .forms import document
import base64
from django.views.decorators.csrf import csrf_exempt
import json 
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
    imgstr = image_data.split('data:image/png;base64,')
    
    decode = base64.b64decode(imgstr)
    
    with ("imagen.png", "wb") as file:
      file.write(decode)
        
  return render(request, 'firm.html')
