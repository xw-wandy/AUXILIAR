import re
from django.shortcuts import render

# Create your views here.

def index(request):
      return render(request, 'auxi/index.html')

def info(request):
      return render(request,'auxi/info.html')


def prestamos(request):
      return render(request,'auxi/prestamos.html')

def inversiones(request):
      return render(request,'auxi/inversiones.html')

def novedad(request):
      return render(request,'auxi/novedad.html')


def ayuda(request):
      return render(request,'auxi/ayuda.html')