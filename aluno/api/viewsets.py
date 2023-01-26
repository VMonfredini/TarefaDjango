from rest_framework import viewsets
from aluno import models
from aluno.api import serializers


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = models.Aluno.objects.all()
    serializer_class = serializers.AlunoSerializers