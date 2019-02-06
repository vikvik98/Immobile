from django.urls import path, include
from usuario.views import RegistrarUsuarioView
from django.contrib.auth import urls

urlpatterns = [
    path('', include(urls)),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
]