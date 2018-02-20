"""
Sistema de Intranet
"""
## @package base.urls
#
# Urls de la aplicación base
# @version 1.0
from django.conf.urls import url
from .views import *
from base import views

urlpatterns = [
    url(r'^$', Inicio.as_view(), name = "inicio"),
]

## Ajax
urlpatterns +=[
    url(r'^ajax/actualizar-combo/?$', actualizar_combo, name='actualizar_combo'),
]
