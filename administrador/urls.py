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
from users.views import RegisterView

urlpatterns = [
    #url(r'^$', Inicio.as_view(), name = "inicio"),
    #url(r'^$', Inicio.as_view(), name = "user"),
    url(r'^datos_empresa$', EmpresaConfigView.as_view(), name = "empresa_datos"),
    url(r'^user/register$', RegisterView.as_view(), name = "user_register"),
    url(r'^cargos/$', CargoList.as_view(), name = "cargo_list"),
    url(r'^cargos/create/$', CargoCreate.as_view(), name = "cargo_create"),
    #url(r'^cargos/update/$', RegisterView.as_view(), name = "user_register"),
    #url(r'^cargos/delete/$', RegisterView.as_view(), name = "user_register"),
]

## Ajax
urlpatterns +=[
]