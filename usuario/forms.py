from django import forms
from django.forms.utils import ErrorList


class PerfilForm(forms.Form):

    nome = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField()
    senha = forms.CharField(max_length=65, widget=forms.PasswordInput)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.lower()
