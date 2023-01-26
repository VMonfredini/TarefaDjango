from rest_framework import serializers
from matricula import models
from aluno.api.serializers import AlunoSerializersMatricula
from disciplina.api.serializers import DisciplinaSerializersMatricula


class MatriculaSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Matricula
        fields = '__all__'


class MatriculaSerializersRA(serializers.ModelSerializer):

    aluno_ra = AlunoSerializersMatricula()
    disciplina_id = DisciplinaSerializersMatricula()

    class Meta:
        model = models.Matricula
        fields = ('aluno_ra', 'npa', 'disciplina_id')