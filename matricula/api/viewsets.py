from rest_framework import viewsets
from matricula import models
from matricula.api import serializers


class MatriculaViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        aluno_ra = self.request.query_params.get('aluno_ra', None)

        if aluno_ra:
            queryset = models.Matricula.objects.filter(aluno_ra=aluno_ra)
            return queryset

        return models.Matricula.objects.all()

    def get_serializer_class(self):
        aluno_ra = self.request.query_params.get('aluno_ra', None)

        if aluno_ra:
            return serializers.MatriculaSerializersRA

        return serializers.MatriculaSerializers
