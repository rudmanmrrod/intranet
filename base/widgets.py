"""
Sistema de Intranet
"""
## @package base.constant
#
# Contiene las clases, atributos y métodos para los widgets a implementar en los formularios
# @version 1.0
from __future__ import unicode_literals

from django.forms import MultiWidget, Select, TextInput
from .constant import SHORT_NACIONALIDAD

class CedulaWidget(MultiWidget):
    """!
    Clase que agrupa los widgets de los campos de nacionalidad y número de cédula de identidad

    @date 26-04-2016
    @version 1.0.0
    """

    def __init__(self, *args, **kwargs):

        widgets = (
            Select(
                attrs={
                    'class': 'col s2', 'data-toggle': 'tooltip',
                    'title': "Seleccione la nacionalidad"
                }, choices=SHORT_NACIONALIDAD
            ),
            TextInput(
                attrs={
                    'class': 'col s10', 'placeholder': '00000000', 'data-mask': '00000000',
                    'data-toggle': 'tooltip', 'maxlength': '8', 'size':'7', 'data-rule-required': 'true',
                    'title': "Indique el número de Cédula de Identidad"
                }
            )
        )

        super(CedulaWidget, self).__init__(widgets, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0], value[1:]]
        return [None, None]