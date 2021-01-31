from django.db import models
from django.contrib import admin
from api.services import calcula_nota

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    media = models.FloatField(default=0, editable=False)

class Gabarito(models.Model):
    questao_1 = models.CharField(max_length=1)
    questao_2 = models.CharField(max_length=1)
    questao_3 = models.CharField(max_length=1)
    questao_4 = models.CharField(max_length=1)
    questao_5 = models.CharField(max_length=1)
    peso_1 = models.IntegerField()
    peso_2 = models.IntegerField()
    peso_3 = models.IntegerField()
    peso_4 = models.IntegerField()
    peso_5 = models.IntegerField()

class Prova(models.Model):
    questao_1 = models.CharField(max_length=1)
    questao_2 = models.CharField(max_length=1)
    questao_3 = models.CharField(max_length=1)
    questao_4 = models.CharField(max_length=1)
    questao_5 = models.CharField(max_length=1)
    nota = models.IntegerField(editable=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    gabarito = models.ForeignKey(Gabarito, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.nota = calcula_nota(self)
        super(Prova, self).save(*args, **kwargs)
        provas = Prova.objects.filter(aluno=self.aluno)
        notas = 0
        for prova in provas:
            notas += prova.nota
        self.aluno.media = notas / provas.count()
        self.aluno.save()

admin.site.register(Aluno)
admin.site.register(Gabarito)
admin.site.register(Prova)