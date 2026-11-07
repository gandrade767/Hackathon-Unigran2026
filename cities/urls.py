from django.urls import path
from cities.views import CidadeListView

app_name = "cidades"

urlpatterns = [
    path("cidades/", CidadeListView.as_view(), name="cidade_list")
]