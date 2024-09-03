from django.db import models

# Create your models here.
class Transacao(models.Model):
    nome_transacao = models.CharField(max_length= 100)
    valor_transacao = models.DecimalField(max_digits=10, decimal_places=2)
    data_transacao = models.DateField(editable=False,auto_now_add=True, verbose_name='data')
    autor_transacao = models.CharField(max_length=100)
    descricao_transacao = models.CharField(max_length=1000, default='valorpadrao')
    
    def __str__(self):
        return f"{self.descricao_transacao} - {self.valor_transacao}"