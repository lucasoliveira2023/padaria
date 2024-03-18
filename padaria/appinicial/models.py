from django.db import models

# Create your models here.
class contato(models.model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.emailField(verbose_name = 'E-mail', max_length=75)
    mensagem = models.TextField(verbose_name = 'Mensagem', max_length=100)
    data =  models.DateTimeFiled(verbose_name = 'data de envio', auto_now_add = True)
    lido = models.BooleanField(verbose_name ='Lido', default=False, blank=True)
    
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    
    class Meta:
        verbose_name = 'Formulario de Contato'
        verbose_plural =  'Formularios de Contatos'
        
    
