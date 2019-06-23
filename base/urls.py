"""
Sistema de Intranet
"""
## @package base.urls
#
# Urls de la aplicación base
# @version 1.0
from django.urls import path
from .views import *
from base import views

app_name = 'base'
urlpatterns = [
    path('', Inicio.as_view(), name = "inicio"),
]

## Ajax
urlpatterns +=[
    path('ajax/actualizar-combo/', actualizar_combo, name='actualizar_combo'),
]
