from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from financeiro.models import Transacao
from financeiro.serializers import TransacaoSerializer
from .forms import TransacaoForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
import json

def list_transacao(request):
    transacoes = Transacao.objects.all()
    #verifica se a requiscao e AJAX ou rest_api e retorna json
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.headers.get ('Content-Type') == 'application/json':
        transacoes_data = list(transacoes.values('data', 'descricao', 'valor'))
        return JsonResponse({'transacoes': transacoes_data}, safe=False)
        
    return render(request, 'lista_transacoes.html', {'transacoes': transacoes})

@csrf_exempt
def create_transaction(request):
    if request.method == 'POST':
        if request.headers.get('x-request-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
            data = json.loads(request.body)
            form = TransacaoForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Transaçao criada com sucesso!'}, status=200)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
            
        else:
            ##para a requisicao nbormal html
            form = TransacaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_transacoes')
            else:
                form = TransacaoForm()
            return render(request, 'lista_transacoes.html', {'form':form})

@csrf_exempt
def get_all_transaction(request):
    if request.method == 'GET':
        
        if request.headers.get('Accept') == 'application/json':
            transacoes = Transacao.objects.all()
            transacoes_data = list(transacoes.values('data', 'descricao', 'valor'))
            return JsonResponse({'transacoes': transacoes_data}, safe=False)
        
        form =TransacaoForm()
        return render(request, 'lista_transacoes.html', {'form':form})     
        

@csrf_exempt
def update_transaction(request, pk):
    transaction = get_object_or_404(Transacao, pk=pk)
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.contend_type == 'aplication/json':
            data = json.loads(request.body)
            form = TransacaoForm(data, instance=transaction)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Transacao autorizada com sucesso!'})
            else:
                return JsonResponse({'erros': form.errors}, status=400)
        else:
            form = TransacaoForm(request.POST, insatance=transaction)
            if form.is_valid():
                form.save()
                return redirect('transaction_list')
            return render(request, 'lista_transacoes.html', {'form': form})

@csrf_exempt
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transacao, pk=pk)
    if request.method == 'POST':##o delete tambem e uma especie de post so recomenda-se usar o post mesmo
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.contend_type == 'aplication/json':
            transaction.delete()
            return JsonResponse({'message': 'Transacao deletada com sucesso!'}, status=204)
        else:
            transaction.delete()
            return redirect('transaction_list')
    return render(request, 'finance/transaction_confirm_delete.html', {'transaction':transaction})