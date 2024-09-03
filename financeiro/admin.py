from django.contrib import admin
from django.contrib import messages
from financeiro.models import Transacao
# Register your models here.

def duplic_transacoes(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None
        obj.save()
    modeladmin.message_user(request,"transacoes duplicadas com sucesso", messages.SUCCESS)    


class TransacaoAdmin(admin.ModelAdmin):
    list_display = ['nome_transacao', 'valor_transacao', 'data_transacao', 'autor_transacao', 'descricao_transacao']
    search_fields = ['descricao_transacao', 'valor_transacao', 'data_transacao']
    list_filter = ['data_transacao']
    action = [duplic_transacoes]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()    

admin.site.register(Transacao, TransacaoAdmin)  

@admin.action(description='Marcar formulario(s) de contato como lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulario(s) de contato(s) marcado(s) como lido(s)', messages.SUCCESS)
    
@admin.action(description='Desmarcar formulario(s) de contato(s) como lido(s)')
def desmarcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formularios de contatos desmarcados', messages.SUCCESS)
