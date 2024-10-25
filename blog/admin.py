from django.contrib import admin
from .models import Categoria, Etiqueta, Articulo, User

# CATEGORIAS
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    search_fields = ("nombre",)
    list_filter = ("activa",)
    ordering = ["nombre", "activa"]

admin.site.register(Categoria, CategoriaAdmin)

# ETIQUETAS
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    search_fields = ("nombre",)
    list_filter = ("activa",)
    ordering = ["nombre", "activa"]

admin.site.register(Etiqueta, EtiquetaAdmin)

# ARTICULOS
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("titulo", "publicado", "categoria", "autor", "creado", "articulo_etiquetas")
    search_fields = ("titulo", "subtitulo", "contenido", "autor__username", "categoria__nombre", "etiquetas__nombre")
    list_filter = ("publicado", "autor", "categoria", "etiquetas")
    readonly_fields = ("creado", "modificado")
    ordering = ["-creado","titulo"]
    autocomplete_fields = ['categoria', 'etiquetas']

    def articulo_etiquetas(self, obj):
        return ' - '.join([t.nombre for t in obj.etiquetas.all().order_by('nombre')])

    articulo_etiquetas.short_description = "Etiquetas"

admin.site.register(Articulo, ArticuloAdmin)
