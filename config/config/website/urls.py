from django.urls import include, path
from .views import index
from rest_framework import routers
from .views import FuncionarioViewSet, ClientesViewSet, ProdutosViewSet

router = routers.DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet, basename="funcionarios")
router.register(r'clientes', ClientesViewSet, basename="clientes")
router.register(r'produtos', ProdutosViewSet, basename="produtos")

urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
