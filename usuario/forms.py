from django import forms
from django.contrib.auth.models import User


class PerfilForm(forms.Form):
    nome = forms.CharField(max_length=50, min_length=4)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField()
    senha = forms.CharField(max_length=65, min_length=3,
                            widget=forms.PasswordInput)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.capitalize()

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        telefone = telefone.replace('-', '').replace('(', "").replace(")", "").replace(" ", "")

        try:
            int(telefone)
            if len(telefone) > 11 or len(telefone) < 10:
                raise ValueError
        except ValueError:
            raise forms.ValidationError('Valor passado é inválido')

        telefone_format = "(" + telefone[0:2] + ") "
        if len(telefone) == 10:
            telefone_format += telefone[2:6] + "-" + telefone[6:10]
        else:
            telefone_format += telefone[2:7] + "-" + telefone[7:11]

        print(telefone)
        return telefone_format

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        users = User.objects.filter(email=email)

        if users:
            raise forms.ValidationError('O e-mail passado já está sendo usado')
        return email
