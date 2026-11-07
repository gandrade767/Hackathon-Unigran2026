from django.urls import path
from area.views import AreaListView

app_name = "areas"

urlpatterns = [
    path("areas/", AreaListView.as_view(), name="area_list"),
]