from rest_framework import viewsets
from serializers import FuncionarioSerializer, ClientesSerializer, ProdutosSerializer
from models import Funcionario, Produtos, Clientes


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('nome')
    serializer_class = FuncionarioSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all().order_by('nome')
    serializer_class = ClientesSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all().order_by('nome')
    serializer_class = ProdutosSerializer
