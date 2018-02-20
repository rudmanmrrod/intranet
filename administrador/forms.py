"""
Sistema de Intranet
"""
## @package administrador.forms
#
# Formulario correspondiente a la aplicación administrador
# @version 1.0
from django import forms
from django.forms import ModelForm
from base.models import Empresa
from base.functions import cargar_entidad, cargar_municipios, cargar_parroquias

class EmpresaForm(ModelForm):
	"""!
	Clase para el formulario de empresa

	@date 18-02-2018
	@version 1.0.0
	"""

	def __init__(self, *args, **kwargs):
		"""!
		Metodo que sobreescribe cuando se inicializa el formulario

		@date 18-02-2018
		@param self <b>{object}</b> Objeto que instancia la clase
		@param args <b>{list}</b> Lista de los argumentos
		@param kwargs <b>{dict}</b> Diccionario con argumentos
		@return Retorna el formulario validado
		"""
		super(EmpresaForm, self).__init__(*args, **kwargs)

		self.fields['estado'].choices = cargar_entidad()
		self.fields['municipio'].choices = cargar_municipios()
		self.fields['parroquia'].choices = cargar_parroquias()

	## estado
	estado = forms.ChoiceField(widget=forms.Select(attrs={
		'onchange': "actualizar_combo(this.value,'base','Municipio','entidad','codigo','nombre','id_municipio');$('select').material_select();"}))

	## municipio
	municipio = forms.ChoiceField(widget=forms.Select(attrs={
		'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','codigo','nombre','id_parroquia');$('select').material_select();"}))

	class Meta:
		model = Empresa
		fields = '__all__'