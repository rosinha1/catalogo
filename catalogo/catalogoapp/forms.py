from dataclasses import field
from django.forms import ModelForm
from django import forms
from catalogoapp.models import Users,Comentario

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'maxlength':'16'
        }))
    usuario = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Usuário',
        'maxlength':'16'
        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'maxlength':'45'
        }))
    nome_loja = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nome da loja',
        'onkeypress': 'regex_nomeloja(event)',
        'maxlength':'45'
        }))
    cnpj = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'CNPJ', 
        'onkeypress': 'regex_cnpj(event)',
        'maxlength':'14'
        }))

    class Meta:
        model = Users
        fields = ['usuario', 'senha', 'email', 'nome_loja', 'cnpj']

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentario 
        fields=['comentario']