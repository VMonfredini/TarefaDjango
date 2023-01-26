from rest_framework import serializers
from disciplina import models


class DisciplinaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = '__all__'


class DisciplinaSerializersProfessor(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ('nome','carga_horaria')


class DisciplinaSerializersMatricula(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ('nome',)