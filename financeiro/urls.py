from django.urls import path
from financeiro import views


urlpatterns = [
    path('/transacoes/', views.list_trasacao, name='lista_transacoes'),
]