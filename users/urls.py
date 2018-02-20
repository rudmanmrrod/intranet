"""
Sistema de Intranet
"""
## @package users.urls
#
# Urls de la aplicación participacion
# @version 1.0
from django.conf.urls import url
from django.contrib.auth.views import *
from .forms import PasswordResetForm, PasswordConfirmForm
from .views import *
from users import views

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name = "login"),
    url(r'^logout$', LogoutView.as_view(), name = "logout"),
    url(r'^register$', RegisterView.as_view(), name = "register"),
    url(r'^update/(?P<pk>\d+)$', PerfilUpdate.as_view(), name = "update"),
    url(r'^password/reset/$', password_reset,
        {'post_reset_redirect': '/password/done/',
         'template_name': 'user.reset.html', 'password_reset_form':PasswordResetForm}, name="reset"),
    url(r'^password/done/$', password_reset_done,
        {'template_name': 'user.passwordreset.done.html'},
        name='reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name': 'user.passwordreset.confirm.html', 'set_password_form':PasswordConfirmForm,
         'post_reset_redirect': '/password/end/'},
        name='password_reset_confirm'),
    url(r'^password/end/$', password_reset_done,
        {'template_name': 'user.passwordreset.end.html'},
        name='reset_end'),
]
