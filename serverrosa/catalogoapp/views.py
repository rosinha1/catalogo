from django.shortcuts import render
from catalogoapp.forms import UsersForm

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def cafe(request):
    return render(request,'sobre.html',{})    


def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)