from django.shortcuts import render

# Create your views here.
from financeiro.models import Transacao

def list_trasacao(request):
    transacoes = Transacao.objects.all()
    return render(request, 'lista_transacoes.html', {'transacoes': transacoes})