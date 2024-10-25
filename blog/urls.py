from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/', views.post, name='post'),
    path('categoria/', views.categoria, name='categoria'),
    path('autor/', views.autor, name='autor'),
    path('fechas/', views.fechas, name='fechas'),

]