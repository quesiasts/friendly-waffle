from rest_framework import viewsets
from .models import Funcionario, Clientes, Produtos
from .serializers import FuncionarioSerializer, ClientesSerializer, ProdutosSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all().order_by('nome')
    serializer_class = FuncionarioSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all().order_by('nome')
    serializer_class = ClientesSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all().order_by('nome')
    serializer_class = ProdutosSerializer
