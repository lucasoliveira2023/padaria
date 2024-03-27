from django.contrib import admin
from django.contrib import messages
# Register your models here.
from appinicial.models import Contato

@admin.action(description='Marcar formulario(s) de contato como lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulario(s) de contato(s) marcado(s) como lido(s)', messages.SUCCESS)
    
@admin.action(description='Desmarcar formulario(s) de contato(s) como lido(s)')
def desmarcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formularios de contatos desmarcados', messages.SUCCESS)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data', 'lido']
    search_fields = ['nome', 'email']
    list_fields = ['data', 'lido']
    actions = [marcar_como_lido]
        