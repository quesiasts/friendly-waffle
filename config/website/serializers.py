from rest_framework import serializers, fields
from .models import Funcionario, Clientes, Produtos

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
