from django.shortcuts import render, redirect
from .models import Tarefa, Pessoa, ResponsavelDaTarefa

def index(request):
    return render(request, 'quadro/index.html')

def detalhe(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    pessoas = Pessoa.objects.all()

    return render(request, 'quadro/detalhe.html', {'tarefa':tarefa, 'pessoas':pessoas})
