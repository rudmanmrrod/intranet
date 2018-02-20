"""
Sistema de Intranet
"""
## @package users.models
#
# Modelos correspondientes a los usuarios
# @version 1.0
from django.db import models
from django.contrib.auth.models import User
from base.models import Parroquia

class Cargos(models.Model):
    """!
    Clase que gestiona los datos de los cargos

    @date 18-02-2018
    @version 1.0.0
    """ 
    ## Nombre del cargo
    nombre = models.CharField(max_length=50,unique=True)

    ## Descripción del cargo
    descripcion = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    """!
    Clase que gestiona los datos de los perfiles

    @date 20-04-2017
    @version 1.0.0
    """    
    ## Número de Cédula
    cedula = models.CharField(max_length=10,unique=True)
    
    ## Relación con la parroquía
    parroquia = models.ForeignKey(Parroquia)

    ## Cargo
    cargo = models.ForeignKey(Cargos)
    
    ## Relación con el user de django
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username