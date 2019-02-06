from django import forms



class AdicionarImovelForm(forms.Form):
    nome = forms.CharField(max_length=50)
    descricao = forms.CharField(max_length=100)
    cep = forms.CharField(max_length=10)
    numero = forms.CharField(max_length=30)
    rua = forms.CharField(max_length=50)
    bairro = forms.CharField(max_length=50)
    cidade = forms.CharField(max_length=50)
    estado = forms.CharField(max_length=50)

