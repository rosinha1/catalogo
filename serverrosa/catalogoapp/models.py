from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=16) #referencia de tabela 
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    ultimo_nome = models.CharField(max_length=16)


