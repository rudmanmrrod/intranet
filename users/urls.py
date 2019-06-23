"""
Sistema de Intranet
"""
## @package users.urls
#
# Urls de la aplicación participacion
# @version 1.0
from django.urls import path
from django.contrib.auth.views import *
from .forms import PasswordResetForm, PasswordConfirmForm
from .views import *
from users import views

app_name = 'users'
urlpatterns = [
    path('login', LoginView.as_view(), name = "login"),
    path('logout', LogoutView.as_view(), name = "logout"),
    path('register', RegisterView.as_view(), name = "register"),
    path('update/<int:pk>', PerfilUpdate.as_view(), name = "update"),
    path('update_profile/<int:pk>', UserPerfilUpdate.as_view(), name = "update_user"),
    path('change_password/', ChangePasswordView.as_view(), name = "change_password"),
    path('constancia-trabajo', ConstanciaPdf.as_view(), name = "constancia"),
]

"""url(r'^password/reset/$', password_reset,
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
    name='reset_end'),"""
