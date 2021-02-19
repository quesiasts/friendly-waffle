from django.urls import include, path
from website import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
]
