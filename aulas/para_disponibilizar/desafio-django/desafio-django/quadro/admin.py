from django.contrib import admin
from .models import Tarefa, Pessoa, ResponsavelDaTarefa

admin.site.register(Tarefa)
admin.site.register(Pessoa)
admin.site.register(ResponsavelDaTarefa)
