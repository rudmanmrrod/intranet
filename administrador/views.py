"""
Sistema de Intranet
"""
## @package administrador.views
#
# Vistas de aplicación administrativa
# @version 1.0

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
	CreateView, UpdateView, ListView, DeleteView,FormView
)
from braces.views import GroupRequiredMixin
from base.models import Empresa, Parroquia
from users.models import Cargos
from .forms import EmpresaForm

class EmpresaConfigView(LoginRequiredMixin,GroupRequiredMixin,FormView):
	"""!
	Muestra el formulario de datos de la empresa

	@date 18-02-2018
	@version 1.0.0
	"""
	template_name = "datos.empresa.html"
	form_class = EmpresaForm
	success_url = reverse_lazy('administrador:empresa_datos')
	success_message = "Se registró con éxito"
	group_required = u"Administrador"

	def get_initial(self):
		"""!
		Metodo para agregar valores de inicio al formulario

		@date 18-02-2018
		@param self <b>{object}</b> Objeto que instancia la clase
		@return Retorna los valores iniciales
		"""
		initial = super(EmpresaConfigView, self).get_initial()
		empresa = Empresa.objects.first()
		if empresa:
			initial['nombre'] = empresa.nombre
			initial['direccion'] = empresa.direccion
			initial['telefono'] = empresa.telefono
			initial['correo'] = empresa.correo
			initial['nombre_encargado'] = empresa.nombre_encargado
			initial['parroquia'] = empresa.parroquia_id
			initial['municipio'] = empresa.parroquia.municipio_id
			initial['estado'] = empresa.parroquia.municipio.entidad_id

		return initial

	def form_valid(self,form):
		"""!
		Metodo que valida si el formulario es valido

		@date 18-02-2018
		@param self <b>{object}</b> Objeto que instancia la clase
		@param form <b>{object}</b> Objeto que contiene el formulario de registro
		@return Retorna el formulario validado
		"""
		empresa = Empresa.objects.first()
		if not empresa:
			empresa = Empresa()

		empresa.nombre = form.cleaned_data['nombre']
		empresa.direccion = form.cleaned_data['direccion']
		empresa.telefono = form.cleaned_data['telefono']
		empresa.nombre_encargado = form.cleaned_data['nombre_encargado']
		empresa.parroquia = form.cleaned_data['parroquia']
		empresa.save()

		return super(EmpresaConfigView, self).form_valid(form)

	def form_invalid(self,form):
		print(form.errors)
		return super(EmpresaConfigView, self).form_invalid(form)


	def form_invalid(self,form):
		print(form.errors)
		return super(EmpresaConfigView, self).form_invalid(form)


class CargoCreate(LoginRequiredMixin,GroupRequiredMixin,SuccessMessageMixin,CreateView):
    """!
    Clase que gestiona la creación de cargos

    @date 18-02-2018
    @version 1.0.0
    """
    model = Cargos
    fields = '__all__'
    template_name = "cargos.create.html"
    success_message = "Se registró el cargo con éxito"
    success_url = reverse_lazy('administrador:cargo_list')
    group_required = u"Administrador"
    

class CargoList(LoginRequiredMixin,GroupRequiredMixin,ListView):
    """!
    Clase que gestiona la lista de cargos

    @date 18-02-2018
    @version 1.0.0
    """
    model = Cargos
    template_name = "cargos.list.html"
    paginate_by = 5
    group_required = u"Administrador"    
    
  
class CargoDelete(LoginRequiredMixin,GroupRequiredMixin,SuccessMessageMixin,DeleteView):
    """!
    Clase que gestiona el borrado de consultas

    @date 20-02-2018
    @version 1.0.0
    """
    model = Cargos
    template_name = "cargos.delete.html"
    success_message = "Se eliminó el cargo con éxito"
    success_url = reverse_lazy('administrador:cargo_list')
    group_required = u"Administrador"
    
    
class CargoUpdate(LoginRequiredMixin,GroupRequiredMixin,SuccessMessageMixin,UpdateView):
    """!
    Clase que gestiona la actualización de cargos

    @date 20-02-2018
    @version 1.0.0
    """
    model = Cargos
    fields = '__all__'
    template_name = "cargos.update.html"
    success_message = "Se actualizó el cargo con éxito"
    success_url = reverse_lazy('administrador:cargo_list')
    group_required = u"Administrador"
    
