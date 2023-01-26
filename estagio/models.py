from django.db import models

# Create your models here.
class Estagio(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_empresa = models.CharField(max_length=45)
    cnpj_empresa = models.CharField(max_length=18)
    carga_horario = models.IntegerField()