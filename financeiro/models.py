from django.db import models

# Create your models here.
class Transacao(models.Model):
    nome_da_trasacao = models.CharField(max_length= 100)
    valor_da_transacao = models.CharField(max_length= 100)
    data_da_transacao = models.DateField(auto_now_add=True)
    autor_da_transacao = models.CharField(max_length=100)