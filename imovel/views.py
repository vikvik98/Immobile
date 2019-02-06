from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from imovel.forms import AdicionarImovelForm
from imovel.models import Imovel


def home(request):
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})



class AdicionarImovelView(View):
    template_post = 'adicionar_imovel.html'

    def get(self, request):
        return render(request, self.template_post)

    def post(self, request):
        adicionar_imovelForm = AdicionarImovelForm(request.POST)

        if adicionar_imovelForm.is_valid():
            imovel = Imovel(nome= adicionar_imovelForm.cleaned_data['nome'],
                            descricao= adicionar_imovelForm.cleaned_data['descricao'],
                            cep= adicionar_imovelForm.cleaned_data['cep'],
                            numero= adicionar_imovelForm.cleaned_data['numero'],
                            rua= adicionar_imovelForm.cleaned_data['rua'],
                            bairro= adicionar_imovelForm.cleaned_data['bairro'],
                            cidade= adicionar_imovelForm.cleaned_data['cidade'],
                            estado= adicionar_imovelForm.cleaned_data['estado'])
            imovel.save()
            return redirect('home')

        return render(request, self.template_post, {'form': adicionar_imovelForm})