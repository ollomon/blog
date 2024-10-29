from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Link, Articulo, Categoria
from django.contrib.auth.models import User
import calendar
from django.utils.translation import gettext as _

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

# Filtrado por Categoría
def categoria(request, categoria_id):
    try:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        #articulos = Articulo.objects.filter(categoria=categoria)
        #context = {"categoria": categoria, "articulos": articulos}
        context = {"categoria": categoria}
        return render(request, 'blog/categoria.html', context)
    except:
        return render(request, 'blog/404.html')

# Filtrado por Autor
def autor(request, autor_id):
    try:
        autor = get_object_or_404(User, id=autor_id)
        #articulos = Articulo.objects.filter(autor=autor)
        #context = {"autor": autor, "articulos": articulos}
        context = {"autor": autor}
        return render(request, 'blog/autor.html', context)
    except:
        return render(request, 'blog/404.html')


# Filtrado por Fechas
def fechas(request, mes_id, ano_id):
    if mes_id > 12 or mes_id < 1:
        return render(request, 'blog/404.html')
    articulos = Articulo.objects.filter(publicado=True, creado__month=mes_id, creado__year=ano_id)
    mes_en_letra = _(calendar.month_name[mes_id]).capitalize()
    context = {"articulos": articulos, "mes": mes_en_letra, "ano": ano_id}
    return render(request, 'blog/fechas.html', context)

