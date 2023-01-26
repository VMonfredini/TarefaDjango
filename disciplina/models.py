from django.db import models

# Create your models here.
class Disciplina(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    conteudo = models.CharField(max_length=300)
    carga_horaria = models.IntegerField()