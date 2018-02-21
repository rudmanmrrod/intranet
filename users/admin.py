"""
Sistema de Intranet
"""
## @package users.admin
#
# Vista donde se registran modelos en el admin
# @version 1.0

from django.contrib import admin
from .models import Perfil

admin.site.register(Perfil)
