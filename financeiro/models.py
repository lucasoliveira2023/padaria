from django.db import models

# Create your models here.
class Transacao(models.Model):
    nome_da_transacao = models.CharField(max_length= 100)
    valor_da_transacao = models.CharField(max_length= 100)
    data_da_transacao = models.DateField(auto_now_add=True, verbose_name='data')
    autor_da_transacao = models.CharField(max_length=100)
    descricao_da_transacao = models.CharField(max_length=1000, default='valorpadrao')