from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
# Create your views here.
from financeiro.models import Transacao
from financeiro.serializers import TransacaoSerializer
from .forms import TransacaoForm

def list_transacao(request):
    transacoes = Transacao.objects.all()
    return render(request, 'lista_transacoes.html', {'transacoes': transacoes})


#class TransacaoListCreate(generics.ListCreateAPIView):
#    queryset = Transacao.objects.all()
#    serializer_class = TransacaoSerializer

def create_transaction(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacoes')
        
        else:
            form = TransacaoForm()
            
        return render(request, 'lista_transacoes.html', {'form': form})
    
def get_all_transaction(request):
    if request.method == 'GET':
        form = TransacaoForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('lista_transacoes')
        
        else:
            form = TransacaoForm()
            
        return render(request, 'lista_transacoes.html', {'form':form})
    

def update_transaction(request, pk):
    transaction = get_object_or_404(Transacao, pk=pk)
    if request.method == 'UPDATE':
        form = TransacaoForm(request.UPDATE, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransacaoForm(instance=transaction)
    return render(request, 'lista_transacoes.html', {'form':form})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transacao, pk=pk)
    if request.method == 'DELETE':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'finance/transaction_confirm_delete.html', {'transaction':transaction})