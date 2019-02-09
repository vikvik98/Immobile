from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View

from imovel.forms import *
from imovel.models import Imovel
from usuario.models import Perfil


@login_required
def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})


@login_required
def item_imovel(request, id_imovel):
    imovel = Imovel.objects.get(id=id_imovel)
    return render(request, 'item_imovel.html', {'imovel': imovel})


def perfil_imoveis(request):
    perfil_logado = get_perfil_logado(request)
    imoveis = perfil_logado.imoveis.all()
    return render(request, 'perfil_imoveis.html', {'imoveis': imoveis})


class AdicionarImovelView(View):
    template_post = 'adicionar_imovel.html'

    def get(self, request):
        form = AdicionarImovelForm()
        return render(request, self.template_post, {'form': form})

    def post(self, request):
        adicionar_imovelForm = AdicionarImovelForm(request.POST, request.FILES)
        perfil_logado = get_perfil_logado(request)

        if adicionar_imovelForm.is_valid():
            imovel = adicionar_imovelForm.save()
            imovel.perfis.add(perfil_logado)
            imovel.save()
            return redirect('home')

        return render(request, self.template_post, {'form': adicionar_imovelForm})


def editar_imovel(request, id):
    imovel = Imovel.objects.get(id=id)
    if request.method == 'GET':
        form = AdicionarImovelForm(instance=imovel)
        return render(request, 'adicionar_imovel.html', {'form': form})

    else:
        adicionar_imovelForm = AdicionarImovelForm(request.POST, request.FILES, instance=imovel)

        if adicionar_imovelForm.is_valid():
            adicionar_imovelForm.save()

            return redirect('item_imovel', id)

        return render(request, 'adicionar_imovel.html', {'form': adicionar_imovelForm})


def get_perfil_logado(request):
    return request.user.perfil


def remover_imovel(request, imovel_id):
    imovel = Imovel.objects.get(id=imovel_id)
    imovel.delete()
    return redirect('perfil_imoveis')


def add_proprietario(request, id):
    imovel = Imovel.objects.get(id=id)
    perfil_list = Perfil.objects.exclude(id__in=imovel.perfis.all())

    if request.method == 'GET':
        form = AddPerfilForm()
        return render(request, 'add_proprietario.html', {'form': form, 'perfil_list': perfil_list})

    else:
        form = AddPerfilForm(request.POST)

        if form.is_valid():
            imovel.perfis.add(form.cleaned_data['perfis'][0])
            return redirect('item_imovel', id)

        return render(request, 'add_proprietario.html', {'form': form, 'perfil_list': perfil_list})
