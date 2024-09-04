from django.urls import path
from financeiro import views
#from .views import  TransacaoListCreate

urlpatterns = [
    path('transacoes/', views.list_transacao, name='lista_transacoes'),
    #path('/transacoes/', TransacaoListCreate.as_views(), name='transacao_list_create'),
]