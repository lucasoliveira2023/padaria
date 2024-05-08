from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from financeiro.models import Transacao
from financeiro.serializers import TransacaoSerializer

def list_transacao(request):
    transacoes = Transacao.objects.all()
    return render(request, 'lista_transacoes.html', {'transacoes': transacoes})


class TransacaoListCreate(generics.ListCreateAPIView):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer