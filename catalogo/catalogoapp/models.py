from tkinter.tix import MAX
from django.db import models

# Create your models here.

class Users(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    email = models.EmailField(max_length=45)
    nome_loja = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=14)

class Comentario(models.Model):
    comentario=models.TextField(max_length=255)
    usuario=models.ForeignKey(Users,on_delete=models.CASCADE)

""" class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16) """