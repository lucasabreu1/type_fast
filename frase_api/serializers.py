from rest_framework import serializers 


class FraseSerializer(serializers.Serializer):
	conteudo = serializers.CharField(max_length=100)

