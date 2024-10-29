from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Link, Articulo, Categoria
from django.contrib.auth.models import User
import calendar
from django.utils.translation import gettext as _

# Página de Inicio
def inicio(request):
    if not request.session.get("items_per_page"):
        request.session['items_per_page'] = 2
    if request.method == 'GET' and 'items_per_page' in request.GET:
        request.session['items_per_page'] = int(request.GET['items_per_page'])
    articulos_por_pagina = request.session['items_per_page']

    articulos_pagina = Paginator(Articulo.objects.filter(publicado=True), articulos_por_pagina)
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
        total_likes = articulo.total_likes()
        liked = False
        if articulo.likes.filter(id=request.user.id).exists():
            # si ya tiene like por parte del usuario
            liked = True
        context = {"articulo": articulo, "total_likes": total_likes, "liked": liked}
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


# Likes en un artículo
def like_articulo(request, articulo_id):
    print("Id del artículo: ", articulo_id)
    articulo = get_object_or_404(Articulo, id=articulo_id) #request.POST.get('articulo_id'))
    if articulo.likes.filter(id=request.user.id).exists():
        # si ya marcó me gusta, lo desmarca
        articulo.likes.remove(request.user)
    else:
        # añade el like del usuario, marca el usuario en el campo like
        articulo.likes.add(request.user)
    # volver a recargar la página del "detalle del artículo" pasándole la id del post
    return HttpResponseRedirect(reverse('post', args=[str(articulo.id)]))