from .models import About, Link, Categoria, Articulo


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
def ctx_dic_historico(request):
    ctx_historico = {}
    # Devuelve las fechas que coinciden en el campo creado con el mes, una sóla vez (distinct), en orden descendiente, es decir, de mayor a menor...
    ctx_historico['FECHAS'] = Articulo.objects.dates('creado', 'month', order='DESC').distinct()
    return ctx_historico


# REDES SOCIALES
def ctx_dic_link(request):
    ctx_link = {}
    links = Link.objects.all()
    for link in links:
        ctx_link[link.key] = {'url': link.url, 'icono': link.icono, 'nombre': link.nombre}
    return ctx_link

# ENTRADAS RECIENTES
def ctx_dic_entradas_recientes(request):
    ctx_entradas = {
        'ENTRADAS': Articulo.objects.only('titulo', 'creado').order_by('-creado')[:3]
    }
    return ctx_entradas