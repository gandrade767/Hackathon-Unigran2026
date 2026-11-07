from django.shortcuts import render
from django.views.generic import ListView
from solicitacao.models import Solicitacoes

# Create your views here.
class SolicitacaoListView(ListView):
    model = Solicitacoes
    template_name = "solicitacao/solicitacao.html"
    context_object_name = "Solicitacoes"
    paginate_by = 10

    