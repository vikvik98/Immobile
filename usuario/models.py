from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):

    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    usuario = models.OneToOneField(User, related_name='perfil',
                                on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email
