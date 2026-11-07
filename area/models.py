from django.db import models
from cities.models import Cidade
# Create your models here.
class Area(models.Model):
    class TipoArea(models.TextChoices):
        RESIDENCIAL = "residencial", "Residencial"
        COMERCIAL = "comercial", "Comercial"
        ESPACO_PUBLICO = "espaco_publico", "Espaço Público"
        VIA_CIRCULACAO = "via_circulacao", "Via de Grande Circulação"

    nome = models.CharField(max_length=50, verbose_name="Nome")
    tipo_area = models.CharField(max_length=30,  choices=TipoArea.choices)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name="Cidade")
    