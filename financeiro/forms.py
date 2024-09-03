from django import forms
from financeiro.models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['nome_transacao', 'valor_transacao', 'autor_transacao', 'descricao_transacao']
