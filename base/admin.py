"""
Sistema de Intranet
"""
## @package administrador.admin
#
# Vista donde se registran modelos en el admin
# @version 1.0
from django.contrib import admin
from .models import Empresa

admin.site.register(Empresa)

