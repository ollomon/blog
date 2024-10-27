from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Link, Articulo

# Página de Inicio
def inicio(request):
    articulos_pagina = Paginator(Articulo.objects.filter(publicado=True), 2)
    pagina = request.GET.get('page')
    articulos = articulos_pagina.get_page(pagina)
    aux = 'x' * articulos.paginator.num_pages
    context = {'articulos': articulos, 'aux': aux}
    return render(request, "blog/inicio.html", context)

# Detalle del artículo
def post(request, articulo_id):
    #articulo = Articulo.objects.get(id=articulo_id)
    try:
        articulo = get_object_or_404(Articulo, id=articulo_id)
        context = {"articulo": articulo}
        return render(request, 'blog/detalle.html', context)
    except:
        return render(request, 'blog/404.html')

def categoria(request):
    return render(request, 'blog/inicio.html')

def autor(request):
    return render(request, 'blog/inicio.html')

def fechas(request):
    return render(request, 'blog/inicio.html')

