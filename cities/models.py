from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado")
    orcamento = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.estado} - {self.orcamento}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
