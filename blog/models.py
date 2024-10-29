from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
import os


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

# Función para limitar el tamaño de la imagen a subir en el artículo
def validar_tamano_imagen(imagen):
    max_size_kb = 2048  # Tamaño máximo en KB (2 MB)
    if imagen.size > max_size_kb * 1024:
        raise ValidationError("La imagen no debe exceder los 2 MB.")

# MODELO DE ARTICULOS (POSTS)
class Articulo(models.Model):
    titulo = models.CharField(max_length=250, verbose_name="Título")
    subtitulo = models.TextField(verbose_name="Subtítulo")
    #contenido = models.TextField(verbose_name="Contenido")
    contenido = RichTextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name="Imagen", validators=[validar_tamano_imagen])
    publicado = models.BooleanField(default=False, verbose_name="Publicado")
    
    # Campos con relaciones
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='get_articulos', verbose_name="Categoría")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_articulos',  verbose_name="Autor")
    etiquetas = models.ManyToManyField(Etiqueta, blank=True, null=True, verbose_name="Etiquetas")

    likes = models.ManyToManyField(User, blank=True, null=True, related_name='blog_articulos', verbose_name="Me Gusta")

    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-creado']
    
    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Si ya existe una imagen y está siendo reemplazada o eliminada
        if self.pk:
            old_imagen = Articulo.objects.get(pk=self.pk).imagen
            if old_imagen and old_imagen != self.imagen:
                old_imagen_path = os.path.join(settings.MEDIA_ROOT, old_imagen.path)
                if os.path.isfile(old_imagen_path):
                    os.remove(old_imagen_path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Eliminar la imagen física cuando se elimina el artículo completo
        if self.imagen and os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super().delete(*args, **kwargs)


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

