from django import forms
from financeiro.models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'data', 'descricao_da_transacao']
