from django.contrib import admin
from cities.models import Cidade
# Register your models here.

@admin.register(Cidade)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "estado", "orcamento",)