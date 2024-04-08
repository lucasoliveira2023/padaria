from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'pginicio.html')


def Contato(request):
<<<<<<< HEAD
    return render(request, 'pgcontato.html')
=======
    return render (request, 'pgcontato.html')
>>>>>>> a8bb9c31f2fd5aa9df7e44a0da2b56394c5d1563
