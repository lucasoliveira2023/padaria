from django.shortcuts import render
from appinicial.forms import ContatoForm
# Create your views here.
def inicio(request):
    return render(request, 'pginicio.html')

def Contato(request):
    success = False
    form = ContatoForm(request.POST or None)
    if form .is_valid():
        success = True
        form.save()
    contexto = {
        'telefone': '68992208221',
        'responsavel': 'lucas',
        'forms':form,
        'sucesso':success,
    }
    return render(request, 'pgcontato.html', contexto)    