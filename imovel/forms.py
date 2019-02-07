from django import forms

from imovel.models import Imovel


class AdicionarImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = ['perfil']
