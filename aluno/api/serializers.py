from rest_framework import serializers
from aluno import models
from estagio.api.serializers import EstagioSerializers


class AlunoSerializers(serializers.ModelSerializer):
    Estagio_id = EstagioSerializers

    class Meta:
        model = models.Aluno
        fields = '__all__'


class AlunoSerializersMatricula(serializers.ModelSerializer):

    class Meta:
        model = models.Aluno
        fields = ('nome',)