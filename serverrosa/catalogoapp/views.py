from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def cafe(request):
    return render(request,'sobre.html',{})    

