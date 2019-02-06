from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import PerfilForm, CustomAuthenticationForm
from .models import Perfil


class RegistrarUsuarioView(View):
    template_name = 'registration/registrar.html'

    def get(self, request):
        form = PerfilForm()
        return render(request, self.template_name, {'form': form})

    @transaction.atomic
    def post(self, request):
        form = PerfilForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['email'],
                                            email=data['email'],
                                            password=data['senha'])
            perfil = Perfil(nome=data['nome'],
                            telefone=data['telefone'],
                            usuario=user)
            perfil.save()
            return redirect('login')

        return render(request, self.template_name, {'form': form})


class MyLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
