"""
URL configuration for padaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appinicial.views import inicio, index, Contato
from financeiro.views import create_transaction, update_transaction, delete_transaction, list_transacao
from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('transacoes/', list_transacao, name='lista_transacoes'),
    #path('', include('myapp.urls')),
    path('pgcontato/', Contato, name='contato'),
    path('admin/', admin.site.urls),
    
    path('create/', create_transaction, name='transaction_create'),
    path('update/<int:pk>/', update_transaction, name='transaction_update'),
    path('delete/<int:pk>/', delete_transaction, name='transaction_delete'),
    
]
