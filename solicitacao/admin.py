from django.contrib import admin
from solicitacao.models import Solicitacoes

# Register your models here.
@admin.register(Solicitacoes)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ("status", "nivel_prioridade", "gasto", "tipo_solicitacao", "data_solicitacao")
    search_fields = ("status",)
    list_filter = ("status", "nivel_prioridade", "tipo_solicitacao")
