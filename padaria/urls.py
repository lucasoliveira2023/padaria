from django.contrib import admin
from django.urls import path, include
from appinicial.views import inicio, index, Contato
from financeiro.views import list_transacao, create_transaction, get_all_transaction, update_transaction, delete_transaction
from financeiro.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('transacoes/', list_transacao, name='lista_transacoes'),
    path('transacoes-all', get_all_transaction, name='get_all_transaction'),
    path('transacoes/criar/', create_transaction, name='transaction_create'),
    path('transacoes/update/<int:pk>/', update_transaction, name='transaction_update'),
    path('transacoes/delete/<int:pk>/', delete_transaction, name='transaction_delete'),
    path('pgcontato/', Contato, name='contato'),
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
