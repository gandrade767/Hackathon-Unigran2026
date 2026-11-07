from django.views.generic import ListView
from cities.models import Cidade

# Create your views here.
class CidadeListView(ListView):
    model = Cidade
    template_name = "cities/cidade_list.html"
    context_object_name = "cidade"