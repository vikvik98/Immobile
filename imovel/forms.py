from django import forms

from imovel.models import Imovel


class AdicionarImovelForm(forms.ModelForm):
    nome = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'}))

    descricao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição'}))
    cep = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cep'}))
    numero = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'numero'}))
    rua = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'rua'}))
    bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bairro'}))
    cidade = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'cidade'}))
    estado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'estado'}))

    class Meta:
        model = Imovel
        exclude = ['perfis']


class AddPerfilForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = ['perfis']
