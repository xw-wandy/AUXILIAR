from . import views
from django.urls import path

app_name = 'aux'
urlpatterns = [
    path('', views.index, name='index'),
    path("info/", views.info, name='info'),
    path("prestamos/", views.prestamos, name='prestamos'),
    path("inversiones/", views.inversiones, name='inversiones'),
    path("novedad/", views.novedad, name='novedad'),
    path("ayuda/", views.ayuda, name='ayuda'),
]
