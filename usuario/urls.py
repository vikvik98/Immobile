from django.contrib.auth.views import LogoutView
from django.urls import path

from usuario.forms import CustomAuthenticationForm
from usuario.views import RegistrarUsuarioView, MyLoginView

urlpatterns = [
    path('login/', MyLoginView.as_view(),
         {'authentication_form': CustomAuthenticationForm}, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
]
