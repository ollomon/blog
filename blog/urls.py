from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:articulo_id>', views.post, name='post'),
    path('categoria/<int:categoria_id>', views.categoria, name='categoria'),
    path('autor/<int:autor_id>', views.autor, name='autor'),
    path('fechas/<int:mes_id>/<int:ano_id>', views.fechas, name='fechas'),

]