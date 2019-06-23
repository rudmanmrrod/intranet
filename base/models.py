"""
Sistema de Intranet
"""
## @package base.models
#
# Modelos correspondientes a la aplicación base
# @version 1.0
from django.db import models

class Entidad(models.Model):
    """!
    Clase que gestiona el modelo de las entidades o estados

    @date 18-04-2017
    @version 1.0.0
    """
    ## Código de la entidad
    codigo = models.CharField(max_length=50)
    
    ## Nombre de la entidad
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    """!
    Clase que gestiona el modelo de los municipios

    @date 18-04-2017
    @version 1.0.0
    """
    ## Código del municipio
    codigo = models.CharField(max_length=50)
    
    ##  Nombre del municipio
    nombre = models.CharField(max_length=50)
    
    ## Relación con la entidad
    entidad = models.ForeignKey(Entidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Parroquia(models.Model):
    """!
    Clase que gestiona el modelo de las parriquias

    @date 18-04-2017
    @version 1.0.0
    """
    ## Código de la parroquia
    codigo = models.CharField(max_length=50)
    
    ## Nombre de la parroquia
    nombre = models.CharField(max_length=50)
    
    ## Relación con el municipio
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    """!
    Clase que gestiona el modelo de los datos de la empresa

    @date 18-04-2017
    @version 1.0.0
    """
    ## Nombre de la empresa
    nombre = models.CharField(max_length=128)
    
    ## Dirección de la empresa
    direccion = models.CharField(max_length=255)

    ## Correo de la empresa
    correo = models.EmailField()
    
    ## telefono
    telefono = models.CharField(max_length=25)

    ## Nombre del Encargado
    nombre_encargado = models.CharField(max_length=128)

    ## Relación con la parroquia
    parroquia = models.ForeignKey(Parroquia,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
