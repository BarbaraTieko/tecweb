from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.titulo}'

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class ResponsavelDaTarefa(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} - {self.tarefa} - {self.pessoa}'
