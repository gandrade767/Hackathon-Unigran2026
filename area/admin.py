from django.contrib import admin
from area.models import Area
# Register your models here.

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo_area")
    search_fields = ("nome", "tipo_area")
    list_filter = ("nome", "tipo_area")
