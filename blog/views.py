from django.shortcuts import render
from .models import Link

# Create your views here.
def inicio(request):
    return render(request, "blog/inicio.html")

def post(request):
    return render(request, 'blog/detalle.html')

def categoria(request):
    return render(request, 'blog/inicio.html')

def autor(request):
    return render(request, 'blog/inicio.html')

def fechas(request):
    return render(request, 'blog/inicio.html')

