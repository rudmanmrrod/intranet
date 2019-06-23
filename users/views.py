"""
Sistema de Intranet
"""
## @package user.views
#
# Vistas correspondientes a la aplicación usuario
# @version 1.0
from django.shortcuts import render, redirect
from django.views.generic import (
    FormView, RedirectView, CreateView, 
    UpdateView, ListView, TemplateView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User, Group
from django.http import HttpResponseForbidden, JsonResponse
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from easy_pdf.views import PDFTemplateView
from datetime import datetime
from .forms import (
    LoginForm, UserRegisterForm, 
    PerfilForm, PasswordChangeForm
    )
from .models import Perfil
from base.models import Parroquia, Empresa



class LoginView(FormView):
    """!
    Clase que gestiona la vista principal del logeo de usuario

    @date 01-03-2017
    @version 1.0.0
    """
    form_class = LoginForm
    template_name = 'user.login.html'
    success_url = reverse_lazy('base:inicio')

    def form_valid(self, form):
        """!
        Metodo que valida si el formulario es valido
    
        @date 01-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """
        usuario = form.cleaned_data['usuario']
        contrasena = form.cleaned_data['contrasena']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        if self.request.POST.get('remember_me') is not None:
            # Session expira a los dos meses si no se deslogea
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)
    
    
class LogoutView(RedirectView):
    """!
    Clase que gestiona la vista principal del deslogeo de usuario

    @date 01-03-2017
    @version 1.0.0
    """
    permanent = False
    query_string = True

    def get_redirect_url(self):
        """!
        Metodo que permite definir la url de dirección al ser válido el formulario
    
        @date 01-03-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la url
        """
        logout(self.request)
        return reverse_lazy('users:login')


class RegisterView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin,FormView):
    """!
    Muestra el formulario de registro de usuarios

    @date 09-01-2017
    @version 1.0.0
    """
    template_name = "user.register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_list')
    success_message = "Se registró con éxito"
    group_required = u"Administrador"
    model = User

    def form_valid(self, form, **kwargs):
        """!
        Metodo que valida si el formulario es valido
    
        @date 20-04-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """
        self.object = form.save()
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['nombre']
        self.object.last_name = form.cleaned_data['apellido']
        self.object.set_password(form.cleaned_data['password'])
        self.object.email = form.cleaned_data['email']
        self.object.save()

        self.object.groups.add(2)
              
        parroquia = Parroquia.objects.get(id=form.cleaned_data['parroquia'])
        
        perfil = Perfil()
        perfil.cedula = form.cleaned_data['cedula']
        perfil.parroquia = parroquia
        perfil.cargo = form.cleaned_data['cargo']
        perfil.sueldo = form.cleaned_data['sueldo']
        perfil.fecha_ingreso = form.cleaned_data['fecha_ingreso']
        perfil.user = self.object
        perfil.save() 
        
        return super(RegisterView, self).form_valid(form)
    
class PerfilUpdate(LoginRequiredMixin,SuccessMessageMixin,GroupRequiredMixin,UpdateView):
    """!
    Clase que gestiona la actualización del perfil

    @date 24-04-2017
    @version 1.0.0
    """
    model = Perfil
    template_name = "perfil.update.html"
    form_class = PerfilForm
    success_message = "Se actualizó el perfil con éxito"
    group_required = u"Administrador"
    
    def get_object(self, queryset=None):
        """
        Metodo para obtener el objeto del perfil
    
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param queryset <b>{object}</b> Objeto que contiene una consulta
        @return El objeto del perfil
        """
        obj = Perfil.objects.get(user_id=self.kwargs['pk'])
        return obj
    
    def get_success_url(self):
        """!
        Metodo que permite definir la url de dirección al ser válido el formulario
    
        @date 24-04-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la url
        """
        return reverse_lazy('users:update',
                            kwargs={'pk': self.kwargs['pk']})
    
    def get_initial(self):
        """!
        Metodo para agregar valores de inicio al formulario
    
        @date 24-04-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna los valores iniciales
        """
        initial = super(PerfilUpdate, self).get_initial()
        perfil = Perfil.objects.get(user_id=self.kwargs['pk'])
        initial['cargo'] = perfil.cargo_id
        initial['nombre'] = perfil.user.first_name
        initial['apellido'] = perfil.user.last_name
        initial['sueldo'] = perfil.sueldo
        #initial['fecha_ingreso'] = str(perfil.fecha_ingreso.strftime('%d/%m/%Y'))
        initial['fecha_ingreso'] = perfil.fecha_ingreso
        initial['parroquia'] = perfil.parroquia_id
        initial['municipio'] = perfil.parroquia.municipio_id
        initial['estado'] = perfil.parroquia.municipio.entidad_id
    
        return initial
    
    def form_valid(self,form):
        """!
        Metodo que valida si el formulario es valido
    
        @date 24-04-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """
        parroquia = Parroquia.objects.get(id=form.cleaned_data['parroquia'])
        
        self.object = form.save()
        self.object.cedula = form.cleaned_data['cedula']
        self.object.sueldo = form.cleaned_data['sueldo']
        self.object.fecha_ingreso = form.cleaned_data['fecha_ingreso']
        self.object.cargo = form.cleaned_data['cargo']
        self.object.parroquia = parroquia
        self.object.save()

        user = User.objects.get(pk=self.kwargs['pk'])
        user.first_name = form.cleaned_data['nombre']
        user.last_name = form.cleaned_data['apellido']
        user.save()
        
        return super(PerfilUpdate, self).form_valid(form)


class UserPerfilUpdate(PerfilUpdate, GroupRequiredMixin):
    group_required = u"Usuario"
    template_name = "perfil.html"

    def dispatch(self, request, *args, **kwargs):
        """
        Metodo que redirecciona al usuario si no cuenta con los permisos
    
        @date 24-04-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param args <b>{object}</b> Objeto que contiene los argumentos
        @param kwargs <b>{object}</b> Objeto que contiene los datos de contexto
        @return: Direcciona al 403 si no es su perfil
        """
        if int(self.request.user.id) != int(self.kwargs['pk']):
            #messages.info(request,'No tienes permiso para hacer esto')
            return HttpResponseForbidden()
        return super(UserPerfilUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """!
        Metodo que permite definir la url de dirección al ser válido el formulario
    
        @date 24-04-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la url
        """
        return reverse_lazy('users:update_user',
                            kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        """!
        Metodo que permite cargar de nuevo valores en los datos de contexto de la vista
    
        @date 20-02-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene los datos de contexto
        @return Retorna los datos de contexto
        """
        kwargs['update_form'] = PasswordChangeForm()
        return super(UserPerfilUpdate, self).get_context_data(**kwargs)


class PerfilList(LoginRequiredMixin,GroupRequiredMixin,ListView):
    """!
    Clase que gestiona la lista de cargos

    @date 18-02-2018
    @version 1.0.0
    """
    model = Perfil
    template_name = "perfil.list.html"
    paginate_by = 10
    group_required = u'Administrador'


class ConstanciaPdf(PDFTemplateView,GroupRequiredMixin):
    """!
    Clase que gestiona la renderización de constancias en PDF

    @date 20-02-2018
    @version 1.0.0
    """
    template_name = 'constancia.pdf.html'
    group_required = u"Usuario"

    def get_context_data(self, **kwargs):
        """!
        Metodo que permite cargar de nuevo valores en los datos de contexto de la vista
    
        @date 20-02-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene los datos de contexto
        @return Retorna los datos de contexto
        """
        perfil = Perfil.objects.get(user_id=self.request.user.id)
        kwargs['name'] = perfil.user.first_name + " " + perfil.user.last_name
        kwargs['cedula'] = perfil.cedula
        kwargs['cargo'] = perfil.cargo.nombre
        kwargs['sueldo'] = perfil.sueldo
        kwargs['fecha_ingreso'] = perfil.fecha_ingreso
        empresa = Empresa.objects.first()
        kwargs['empresa'] = empresa.nombre
        kwargs['empleador'] = empresa.nombre_encargado
        kwargs['correo'] = empresa.correo
        kwargs['direccion'] = empresa.direccion
        kwargs['telefono'] = empresa.telefono
        kwargs['fecha'] = datetime.now()
        return super(ConstanciaPdf, self).get_context_data(**kwargs)


class ChangePasswordView(LoginRequiredMixin,TemplateView):
    """!
    Clase que gestiona el borrado de una pregunta

    @date 20-02-2018
    @version 1.0.0
    """
    template_name = "change_password.form.html"
    
    def post(self, request):
        """!
        Metodo que sobreescribe la acción por POST
    
        @date 20-02-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param pk <b>{int}</b> Recibe el id del perfil
        @return Retorna los datos de contexto
        """
        perfil = Perfil.objects.filter(user_id=int(request.user.id))
        if perfil:
            perfil = perfil.get()
            old_p = request.POST.get('old_password','')
            new_p = request.POST.get('new_password','')
            new_rp = request.POST.get('new_password_repeat','')
            if old_p=='' or new_p=='' or new_rp=='':
                return JsonResponse({'success':False,'mensaje':'Datos Vacíos'})
            elif new_p != new_rp:
                return JsonResponse({'success':False,'mensaje':'Las contraseñas no coinciden'})
            elif not check_password(old_p,perfil.user.password):
                return JsonResponse({'success':False,'mensaje':'La contraseña anterior es inválida'})
            else:
                perfil.user.set_password(new_p)
                perfil.user.save()
                return JsonResponse({'success':True,'mensaje':'Se cambió la contraseña con éxito'})
        else:
            return JsonResponse({'success':False,'mensaje':'Perfil Invalido'})