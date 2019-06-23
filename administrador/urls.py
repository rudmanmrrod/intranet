"""
Sistema de Intranet
"""
## @package administrador.urls
#
# Urls de la aplicación administrador
# @version 1.0
from django.urls import path
from .views import *
#from base import views
from users.views import RegisterView, PerfilList, PerfilUpdate

app_name = 'administrador'
urlpatterns = [
    #url(r'^$', Inicio.as_view(), name = "inicio"),
    #url(r'^$', Inicio.as_view(), name = "user"),
    path('datos_empresa', EmpresaConfigView.as_view(), name = "empresa_datos"),
    path('users', PerfilList.as_view(), name = "user_list"),
    path('users/register', RegisterView.as_view(), name = "user_register"),
    path('users/update/<int:pk>', PerfilUpdate.as_view(), name = "user_update"),
    path('cargos/', CargoList.as_view(), name = "cargo_list"),
    path('cargos/create/', CargoCreate.as_view(), name = "cargo_create"),
    path('cargos/update/<int:pk>', CargoUpdate.as_view(), name = "cargo_update"),
    path('cargos/delete/<int:pk>', CargoDelete.as_view(), name = "cargo_delete"),
]

## Ajax
urlpatterns +=[
]