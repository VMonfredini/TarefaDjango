from rest_framework import serializers
from estagio import models


class EstagioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Estagio
        fields = '__all__'