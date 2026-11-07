from django.db import models
from area.models import Area

# Create your models here.
class Solicitacoes(models.Model):
    # Classe para choices
    class ChoicesStatus(models.TextChoices):
        PENDENTE = 'P', 'PENDENTE'
        ANALISE = 'A', 'ANALISE' #ANALISE DAS INFORMAÇÕES
        VISTORIA = 'V', 'VISTORIA'# VISITA TECNICA NO LOCAL
        FINALIZADO = 'F', 'FINALIZADO'
    class ChoicesPrioridade(models.IntegerChoices):
        LEVE = 1 , '1'
        MODERADO = 2, '2'
        GRAVE = 3, '3'
        URGENTE = 4, '4'
    class ChoicesTipo(models.TextChoices):
       ILIMINACAO = 'I', 'ILUMINAÇÃO'
       PAVIMENTACAO = 'P', 'PAVIMENTAÇÃO'
       COLETA_LIXO = 'C', 'COLETA DE LIXO'
       SANEAMENTO = 'S', 'SANEAMENTO BASICO'

    status = models.CharField(max_length=1, choices=ChoicesStatus.choices, default=ChoicesStatus.PENDENTE)

    nivel_prioridade = models.IntegerField(choices=ChoicesPrioridade.choices)

    gasto = models.DecimalField(max_digits=6,verbose_name= "Gasto da solicitação", decimal_places=2)

    tipo_solicitacao = models.CharField(max_length=20, choices=ChoicesTipo.choices)
    
    data_solicitacao = models.DateField(verbose_name="Data de inicio da solicitação")
    data_fim = models.DateTimeField(verbose_name="Data fim da solicitação", blank=True, null=True)

    rua = models.CharField(max_length=200, verbose_name="Nome da Rua", blank=False)

    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name="solicitacoes", verbose_name="Região da solicitação")
    
    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"
        ordering = ["data_solicitacao"]

    def __str__(self):
        return f"{self.status} {self.nivel_prioridade}"