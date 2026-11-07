# Munix · Gestão Municipal Inteligente

Projeto desenvolvido para o Hackathon.

## Tema

Gestão de manutenção urbana: os pedidos dos moradores (iluminação, pavimentação, coleta de lixo e saneamento) ficam reunidos em uma única plataforma, organizados por região e por gravidade.

## Objetivo

- Acompanhar as solicitações dos moradores, com prioridade, situação e custo;
- ver quais regiões têm mais problemas em aberto;
- acompanhar o orçamento disponível, o valor gasto e o andamento das manutenções em uma página de análises.

## Rotas

| Rota | Página |
|---|---|
| `/` | Home: regiões com mais pedidos abertos e pedidos recentes |
| `/analises/` | Análises: orçamento, gastos, situação das manutenções e desempenho por região |
| `/solicitacoes/solicitacoes/` | Lista de solicitações (paginada) |
| `/cidade/cidades/` | Lista de cidades e orçamento |
| `/area/areas/` | Lista de regiões (áreas) da cidade |
| `/admin/` | Painel administrativo para cadastrar cidades, regiões e solicitações |

## Tecnologias usadas

- Python 3
- Django 6.1
- SQLite (banco de dados)
- Django Jazzmin (tema do painel admin)
- Bootstrap 5.3 e Bootstrap Icons (frontend)
- HTML com templates do Django e gráficos em SVG

## Como rodar

1. Crie e ative o ambiente virtual:

   ```bash
   python -m venv .venv
   ```

   ```bash
   .venv\Scripts\activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Aplique as migrações do banco:

   ```bash
   python manage.py migrate
   ```

4. (Opcional) Crie um usuário para acessar o `/admin/`:

   ```bash
   python manage.py createsuperuser
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

6. Acesse <http://127.0.0.1:8000/> no navegador.

## Participantes

| Nome | RGM |
|---|---|
| Gabriel Andrade | 114.073 |
| Guilherme Graces | 114.072 |
| Marcos Portales | 114.017 |
| Gabriel Soares | Aluno |
