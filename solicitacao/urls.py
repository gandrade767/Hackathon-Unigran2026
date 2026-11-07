from django.urls import path
from solicitacao.views import SolicitacaoListView

app_name = "solicitacao"

urlpatterns = [
    path("solicitacoes/", SolicitacaoListView.as_view(), name="solicitacao_list")
]