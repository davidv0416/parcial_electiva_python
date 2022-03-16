from django import views
from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('formulario',views.formulario,name="formulario"),
    path('calcular', views.calcular, name="calcular"),
]
