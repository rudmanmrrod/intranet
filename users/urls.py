"""
Sistema de Intranet
"""
## @package users.urls
#
# Urls de la aplicación participacion
# @version 1.0
from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, 
    PasswordResetConfirmView, PasswordResetCompleteView
)
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
    path('password/reset/',PasswordResetView.as_view(
        template_name='user.reset.html',
        form_class=PasswordResetForm,
        success_url='/password/done/',
        email_template_name="email.password.recover.html"), name="reset"),
    path('password/done/',PasswordResetDoneView.as_view(
        template_name="user.passwordreset.done.html"),name="rest_done"),
    path('password/reset/<str:uidb64>/<str:token>/',PasswordResetConfirmView.as_view(
        template_name="user.passwordreset.confirm.html",
        success_url="/password/done"),name="password_reset_confirm"),
    path('password/done',PasswordResetCompleteView.as_view(
        template_name="user.passwordreset.end.html"),name='password_done')
]