from django.urls import path
from usuario.views import *

urlpatterns = [

    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
]