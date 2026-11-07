from datetime import timedelta
from decimal import Decimal

from django.db.models import Count, Q, Sum
from django.utils import timezone
from django.views.generic import ListView, TemplateView

from area.models import Area
from cities.models import Cidade
from solicitacao.models import Solicitacoes

FINALIZADO = Solicitacoes.ChoicesStatus.FINALIZADO


class AreaListView(ListView):
    model = Area
    template_name = "area/area_list.html"
    context_object_name = "areas"


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Regiões com mais pedidos em aberto (tudo que ainda não foi finalizado)
        context["regioes"] = (
            Area.objects.select_related("cidade")
            .annotate(abertos=Count("solicitacoes", filter=~Q(solicitacoes__status=FINALIZADO)))
            .order_by("-abertos", "nome")[:4]
        )

        # Últimos pedidos registrados
        context["recentes"] = (
            Solicitacoes.objects.select_related("area")
            .order_by("-data_solicitacao", "-pk")[:5]
        )
        return context


class AnaliseView(TemplateView):
    template_name = "analise.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        solicitacoes = Solicitacoes.objects.all()

        # ---- KPIs ----
        orcamento = Cidade.objects.aggregate(total=Sum("orcamento"))["total"] or Decimal("0")
        gasto = solicitacoes.aggregate(total=Sum("gasto"))["total"] or Decimal("0")
        total = solicitacoes.count()
        finalizadas = solicitacoes.filter(status=FINALIZADO).count()
        context.update(
            orcamento_total=orcamento,
            gasto_total=gasto,
            orcamento_restante=orcamento - gasto,
            total_solicitacoes=total,
            finalizadas=finalizadas,
            pendentes=total - finalizadas,
        )

        # ---- Rosca: situação das manutenções ----
        concluidas = finalizadas
        andamento = solicitacoes.filter(status__in=["A", "V"]).count()
        aguardando = solicitacoes.filter(status="P").count()

        def pct(valor):
            return round(valor * 100 / total) if total else 0

        p_concl, p_and = pct(concluidas), pct(andamento)
        p_pend = 100 - p_concl - p_and if total else 0
        context["situacao"] = {
            "concluidas": p_concl,
            "andamento": p_and,
            "pendentes": p_pend,
            # deslocamentos usados no stroke-dashoffset do SVG
            "offset_andamento": -p_concl,
            "offset_pendentes": -(p_concl + p_and),
        }

        # ---- Barras e tabela por região ----
        por_area = list(
            Area.objects.annotate(
                total=Count("solicitacoes"),
                finalizados=Count("solicitacoes", filter=Q(solicitacoes__status=FINALIZADO)),
                gastos=Sum("solicitacoes__gasto"),
            ).order_by("-total", "nome")
        )
        maior = max((a.total for a in por_area), default=0)
        for a in por_area:
            # altura da barra (máx. 191px dentro de um SVG de 200px)
            a.altura = round(a.total * 191 / maior) if maior else 0
            a.y = 200 - a.altura
            a.gastos = a.gastos or Decimal("0")
        context["por_area"] = por_area

        # ---- Linha: solicitações dos últimos 30 dias ----
        hoje = timezone.localdate()
        inicio = hoje - timedelta(days=29)
        por_dia = dict(
            solicitacoes.filter(data_solicitacao__range=(inicio, hoje))
            .values_list("data_solicitacao")
            .annotate(n=Count("id"))
        )
        dias = [inicio + timedelta(days=i) for i in range(30)]
        valores = [por_dia.get(d, 0) for d in dias]
        pico = max(valores) or 1
        pontos = [(round(i * 316 / 29, 1), round(100 - v * 100 / pico, 1)) for i, v in enumerate(valores)]
        ultimos_30 = sum(valores)
        anteriores_30 = solicitacoes.filter(
            data_solicitacao__range=(inicio - timedelta(days=30), inicio - timedelta(days=1))
        ).count()
        context.update(
            ultimos_30=ultimos_30,
            variacao_30=(round((ultimos_30 - anteriores_30) * 100 / anteriores_30) if anteriores_30 else None),
            linha_pontos=" ".join(f"{x},{y}" for x, y in pontos),
            linha_area=" ".join(f"{x},{y}" for x, y in pontos) + " 316,108 0,108",
            linha_rotulos=[dias[0], dias[10], dias[20], dias[29]],
        )
        return context
