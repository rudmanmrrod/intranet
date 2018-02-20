"""
Sistema de Intranet
"""
## @package administrador.urls
#
# Urls de la aplicación administrador
# @version 1.0
from django.conf.urls import url
from .views import *
#from base import views
from users.views import RegisterView, PerfilList, PerfilUpdate

urlpatterns = [
    #url(r'^$', Inicio.as_view(), name = "inicio"),
    #url(r'^$', Inicio.as_view(), name = "user"),
    url(r'^datos_empresa$', EmpresaConfigView.as_view(), name = "empresa_datos"),
    url(r'^users$', PerfilList.as_view(), name = "user_list"),
    url(r'^users/register$', RegisterView.as_view(), name = "user_register"),
    url(r'^users/update/(?P<pk>\d+)$', PerfilUpdate.as_view(), name = "user_update"),
    url(r'^cargos/$', CargoList.as_view(), name = "cargo_list"),
    url(r'^cargos/create/$', CargoCreate.as_view(), name = "cargo_create"),
    url(r'^cargos/update/(?P<pk>\d+)$', CargoUpdate.as_view(), name = "cargo_update"),
    url(r'^cargos/delete/(?P<pk>\d+)$', CargoDelete.as_view(), name = "cargo_delete"),
]

## Ajax
urlpatterns +=[
]