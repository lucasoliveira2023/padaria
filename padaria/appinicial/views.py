from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'pginicio.html')


def Contato(request):
    return render(request, 'pgcontato.html')
