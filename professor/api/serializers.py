from rest_framework import serializers
from professor import models
from disciplina.api.serializers import DisciplinaSerializersProfessor


class ProfessorSerializers(serializers.ModelSerializer):
    disciplina_id = DisciplinaSerializersProfessor()

    class Meta:
        model = models.Professor
        fields = '__all__'