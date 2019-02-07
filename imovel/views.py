from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View

from imovel.forms import AdicionarImovelForm
from imovel.models import Imovel


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
            imovel = adicionar_imovelForm.save(commit=False)
            imovel.perfil = perfil_logado
            imovel.save()

            return redirect('home')
        for a in request.FILES.keys():
            print(a)

        return render(request, self.template_post, {'form': adicionar_imovelForm})


def get_perfil_logado(request):
    return request.user.perfil
