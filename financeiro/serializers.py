from rest_framework import serializers
from financeiro.models import Transacao

class TransacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transacao
        fields = '__all__'
