"""
Sistema de Intranet
"""
## @package base.views
#
# Vistas correspondientes a la aplicación base
# @version 1.0
from django.http import HttpResponse
from django.apps import apps
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import json

    
class Inicio(LoginRequiredMixin,TemplateView):
    """!
    Clase para mostrar el inicio del sistema

    @date 24-04-2017
    @version 1.0.0
    """
    template_name = "inicio.html"


def actualizar_combo(request):
    """!
    Función que actualiza los datos de un select dependiente de los datos de otro select

    @date 28-04-2016
    @param request <b>{object}</b> Objeto que contiene la petición
    @return Devuelve un HttpResponse con el JSON correspondiente a los resultados de la consulta y los respectivos
            elementos a cargar en el select
    """
    try:
        if not request.is_ajax():
            return HttpResponse(json.dumps({'resultado': False, 'error': str('La solicitud no es ajax')}))

        ## Valor del campo que ejecuta la acción
        cod = request.GET.get('opcion', None)

        ## Nombre de la aplicación del modelo en donde buscar los datos
        app = request.GET.get('app', None)

        ## Nombre del modelo en el cual se va a buscar la información a mostrar
        mod = request.GET.get('mod', None)
        
        ## Atributo por el cual se va a filtrar la información
        campo = request.GET.get('campo', None)

        ## Atributo del cual se va a obtener el valor a registrar en las opciones del combo resultante
        n_value = request.GET.get('n_value', None)

        ## Atributo del cual se va a obtener el texto a registrar en las opciones del combo resultante
        n_text = request.GET.get('n_text', None)

        ## Nombre de la base de datos en donde buscar la información, si no se obtiene el valor por defecto es default
        bd = request.GET.get('bd', 'default')

        filtro = {}

        if app and mod and campo and n_value and n_text and bd:
            modelo = apps.get_model(app, mod)
            
            if cod:
                filtro = {campo: cod}

            out = "<option value=''>%s...</option>" % str("Seleccione")

            combo_disabled = "false"

            if cod != "" and cod != "0":
                for o in modelo.objects.using(bd).filter(**filtro).order_by(n_text):
                    out = "%s<option value='%s'>%s</option>" \
                          % (out, str(o.__getattribute__(n_value)),
                             o.__getattribute__(n_text))
            else:
                combo_disabled = "true"

            return HttpResponse(json.dumps({'resultado': True, 'combo_disabled': combo_disabled, 'combo_html': out}))

        else:
            return HttpResponse(json.dumps({'resultado': False,
                                            'error': str('No se ha especificado el registro')}))

    except Exception as e:
        return HttpResponse(json.dumps({'resultado': False, 'error': e}))
