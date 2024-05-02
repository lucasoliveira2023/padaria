from django.shortcuts import render

# Create your views here.
from financeiro.models import Transacao

def list_transacao(request):
    transacoes = Transacao.objects.all()
    return render(request, 'lista_transacoes.html', {'transacoes': transacoes})