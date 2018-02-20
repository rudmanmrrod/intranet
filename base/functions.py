"""
Sistema de Intranet
"""
## @package base.functions
#
# Clases genéricas de la consulta
# @version 1.0
from __future__ import unicode_literals
from django.contrib.auth.models import User
from .models import Entidad, Municipio, Parroquia
from users.models import Perfil

def cargar_entidad():
    """!
    Función que permite cargar todas las entidades

    @date 20-04-2017
    @return Devuelve una tupla con las entidades
    """

    lista = ('', 'Seleccione...'),

    try:
        for entidad in Entidad.objects.all():
            lista += (entidad.codigo, entidad.nombre),
    except Exception as e:
        pass

    return lista


def cargar_municipios():
    """!
    Función que permite cargar todas los municipios

    @date 20-04-2017
    @return Devuelve una tupla con los municipios
    """

    lista = ('', 'Seleccione...'),

    try:
        for municipio in Municipio.objects.all():
            lista += (municipio.codigo, municipio.nombre),
    except Exception as e:
        pass

    return lista


def cargar_parroquias():
    """!
    Función que permite cargar todas las parroquias

    @date 20-04-2017
    @return Devuelve una tupla con las parroquias
    """

    lista = ('', 'Seleccione...'),

    try:
        for parroquia in Parroquia.objects.all():
            lista += (parroquia.codigo, parroquia.nombre),
    except Exception as e:
        pass

    return lista


def validate_cedula(cedula):
    """!
    Función que permite validar la cedula

    @date 20-04-2017
    @param cedula {str} Recibe el número de cédula
    @return Devuelve verdadero o falso
    """
    
    cedula = Perfil.objects.filter(cedula=cedula)
    if cedula:
        return True
    else:
        return False
    
def validate_email(email):
    """!
    Función que permite validar la cedula

    @date 20-04-2017
    @param cedula {str} Recibe el número de cédula
    @return Devuelve verdadero o falso
    """
    
    email = User.objects.filter(email=email)
    if email:
        return True
    else:
        return False
    
def validate_username(username):
    """!
    Función que permite validar el nombre de usuario

    @date 20-09-2017
    @param username {str} Recibe el nombre de usuario
    @return Devuelve verdadero o falso
    """
    
    usr = User.objects.filter(username=username)
    if usr:
        return True
    else:
        return False
    