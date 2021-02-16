from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)


class Clientes(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)


class Produtos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    produto = models.ManyToManyField(Clientes)
