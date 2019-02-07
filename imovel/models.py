from django.db import models

from usuario.models import Perfil


class Imovel(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100)
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=30)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    perfis = models.ManyToManyField(Perfil, related_name='imoveis')
    imagem = models.FileField(upload_to='imovel/', default='imovel/default.jpg')
