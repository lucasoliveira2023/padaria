from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework.views import APIView
# Create your views here.
from financeiro.models import Transacao
from financeiro.serializers import TransacaoSerializer
from .forms import TransacaoForm


def list_transacao(request):
    transacoes = Transacao.objects.all()
    return render(request, 'lista_transacoes.html', {'transacoes': transacoes})
class TransactionList(APIView):
    @csrf_exempt
    def create_transaction(request):
        if request.method == 'POST':
            form = TransacaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_transacoes')
            
            else:
                form = TransacaoForm()
                
            return render(request, 'lista_transacoes.html', {'form': form})
    @csrf_exempt
    def get_all_transaction(request):
        if request.method == 'GET':
            form = TransacaoForm(request.GET)
            if form.is_valid():
                form.save()
                return redirect('lista_transacoes')
            
            else:
                form = TransacaoForm()
                
            return render(request, 'lista_transacoes.html', {'form':form})
        
    @csrf_exempt
    def update_transaction(request, pk):
        transaction = get_object_or_404(Transacao, pk=pk)
        if request.method == 'POST':
            form = TransacaoForm(request.POST, instance=transaction)
            if form.is_valid():
                form.save()
                return redirect('transaction_list')
        else:
            form = TransacaoForm(instance=transaction)
        return render(request, 'lista_transacoes.html', {'form':form})

    @csrf_exempt
    def delete_transaction(request, pk):
        transaction = get_object_or_404(Transacao, pk=pk)
        if request.method == 'POST': ##o delete tambem e uma especie de post so recomenda-se usar o post mesmo
            transaction.delete()
            return redirect('transaction_list')
        return render(request, 'finance/transaction_confirm_delete.html', {'transaction':transaction})