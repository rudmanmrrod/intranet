"""
Sistema de Intranet
"""
## @package base.fields
#
# Contiene las clases, atributos y métodos para los campos personalizados a implementar en los formularios
# @version 1.0
from django.forms import MultiValueField, ChoiceField, CharField

from .constant import SHORT_NACIONALIDAD
from .widgets import CedulaWidget

class CedulaField(MultiValueField):
    """!
    Clase que agrupa los campos de la nacionalidad y número de cédula de identidad en un solo campo del formulario

    @version 1.0.0
    """
    widget = CedulaWidget
    default_error_messages = {
        'invalid_choices': "Debe seleccionar una nacionalidad válida"
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': "Debe indicar un número de Cédula",
            'invalid': "El valor indicado no es válido",
            'incomplete': "El número de Cédula esta incompleto"
        }

        fields = (
            ChoiceField(choices=SHORT_NACIONALIDAD),
            CharField(max_length=8)
        )

        label = "Cedula de Identidad:"

        super(CedulaField, self).__init__(
            error_messages=error_messages, fields=fields, label=label, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ''.join(data_list)
        return ''
    