from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  # return render(request, 'index.html')
  return HttpResponse("world!")

def frank(request):
  return HttpResponse("Frank is here!")
