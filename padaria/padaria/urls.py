from django.contrib import admin
from django.urls import path
from appinicial.views import inicio, Contato

urlpatterns = [
<<<<<<< HEAD
    path('', inicio),
    path('pgcontato/', Contato),
=======
    path('', inicio, name='inicio'),
    path('pgcontato/', Contato, name='contato'),
>>>>>>> a8bb9c31f2fd5aa9df7e44a0da2b56394c5d1563
    path('admin/', admin.site.urls),
]