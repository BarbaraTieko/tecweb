from django.shortcuts import render, redirect
from .models import Memory


def index(request):
    if request.method == 'POST':
        memoria = request.POST.get('memoria')
        Memory.objects.create(texto=memoria)
        return redirect('index')
    else:
        memoria = Memory.objects.last()
        return render(request, 'memories/index.html', {'memoria': memoria})
