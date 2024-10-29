from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# MODELO CATEGORIAS
class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
    activa = models.BooleanField(default=True, verbose_name="Activa:")
    creada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    modificada = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

# MODELO ETIQUETAS
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
    activa = models.BooleanField(default=True, verbose_name="Activa:")
    creada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    modificada = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

# MODELO AUTOR - USUARIOS REGISTRADOS EN LA APLICACIÓN --> Importado de la tabla de usuarios

# MODELO DE ARTICULOS (POSTS)
class Articulo(models.Model):
    titulo = models.CharField(max_length=250, verbose_name="Título")
    subtitulo = models.TextField(verbose_name="Subtítulo")
    #contenido = models.TextField(verbose_name="Contenido")
    contenido = RichTextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name="Imagen")
    publicado = models.BooleanField(default=False, verbose_name="Publicado")
    
    # Campos con relaciones
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='get_articulos', verbose_name="Categoría")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_articulos',  verbose_name="Autor")
    etiquetas = models.ManyToManyField(Etiqueta, verbose_name="Etiquetas")

    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-creado']
    
    def __str__(self):
        return self.titulo
    

# MODELO ABOUT (Acerca de...)
class About(models.Model):
    descripcion = models.CharField(max_length=350, verbose_name="Descripción")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")

    class Meta:
        verbose_name = "Acerca de"
        verbose_name_plural = "Acerca de Nosotros"
        ordering = ['-creado']
    
    def __str__(self):
        return self.descripcion


# MODELO LINKS = REDES SOCIALES
class Link(models.Model):
    key = models.CharField(max_length=100, default="LINK_" ,verbose_name="Key Link")
    nombre = models.CharField(max_length=120, verbose_name="Red Social")
    url = models.URLField(max_length=350, blank=True, null=True, verbose_name="Enlace")
    icono = models.CharField(max_length=100, blank=True, null=True, verbose_name="Icono")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

