from django.urls import path
from . import views

app_name = 'quadro'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detalhe/<int:tarefa_id>', views.detalhe, name = 'detalhe'),
]
