from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f'Funcionario {self.nome}'
        

class Clientes(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)

    def __str__(self):
	    return f'Clientes {self.nome}'


class Produtos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    produto = models.ManyToManyField(Clientes)

    def __str__(self):
	    return f'Produtos {self.nome}'
