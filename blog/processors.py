from .models import About, Link, Categoria


# ------------------- Content Processors ---------------------


# ABOUT - Acerca de
def ctx_dic_about(request):
    ctx_about = {}
    ctx_about['ABOUT'] = About.objects.latest('creado')
    return ctx_about

# CATEGORIAS
def ctx_dic_categorias(request):
    ctx_categorias = {}
    ctx_categorias["CATEGORIAS"] = Categoria.objects.filter(activa=True)
    return ctx_categorias

# ARCHIVOS

# REDES SOCIALES
def ctx_dic_link(request):
    ctx_link = {}
    links = Link.objects.all()
    for link in links:
        ctx_link[link.key] = {'url': link.url, 'icono': link.icono, 'nombre': link.nombre}
    return ctx_link

