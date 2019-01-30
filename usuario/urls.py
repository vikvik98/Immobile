from django.urls import path
from usuario.views import RegistrarUsuarioView

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
]