from django.shortcuts import render, redirect
from .models import FunFacts
from random import choice

def index(request):
    if request.method == 'POST':
        funfact = FunFacts(text=request.POST.get('texto'))
        funfact.save()
        return redirect('index')
    else:
        funfact = FunFacts.objects.all()
        if len(funfact)>0:
            funfact = choice(funfact)
        total = FunFacts.objects.count()
        return render(request, 'funfacts/index.html', {'funfact': funfact, 'total':total})
