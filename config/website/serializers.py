from rest_framework import serializers
from models import Funcionario, Clientes, Produtos

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        field = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        field = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        field = '__all__'
