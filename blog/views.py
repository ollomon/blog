from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Link, Articulo

# Create your views here.
def inicio(request):
    articulos_pagina = Paginator(Articulo.objects.filter(publicado=True), 2)
    pagina = request.GET.get('page')
    articulos = articulos_pagina.get_page(pagina)
    aux = 'x' * articulos.paginator.num_pages
    context = {'articulos': articulos, 'aux': aux}
    return render(request, "blog/inicio.html", context)

def post(request):
    return render(request, 'blog/detalle.html')

def categoria(request):
    return render(request, 'blog/inicio.html')

def autor(request):
    return render(request, 'blog/inicio.html')

def fechas(request):
    return render(request, 'blog/inicio.html')

