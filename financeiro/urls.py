from django.urls import path
from financeiro import views


urlpatterns = [
    path('/transacoes/', views.list_transacao, name='lista_transacoes'),
]