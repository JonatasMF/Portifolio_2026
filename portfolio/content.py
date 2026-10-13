"""
TODO O CONTEÚDO DO SITE FICA AQUI.

Edite os textos, salve e atualize o navegador (o servidor de desenvolvimento
recarrega sozinho). Não precisa mexer em HTML para trocar textos, links ou
projetos.

Arquivos que você pode trocar:
  portfolio/static/portfolio/img/foto.jpg                    -> sua foto
  portfolio/static/portfolio/docs/curriculo-...pdf            -> seu currículo
"""

# ---------------------------------------------------------------------------
# Pessoa
# ---------------------------------------------------------------------------
PESSOA = {
    "nome": "Jônatas Marques de Farias",
    "titulo": "Analista de dados e BI",
    "frase": "Dashboards, análises e automações",
    "sobre": [
        "Trabalho no mercado de dados há 3 anos. Em toda a minha trajetória, o foco foi entregar "
        "informação de qualidade para elevar o nível das áreas de negócio.",
        "Tenho perfil analítico, foco em resultados e bom relacionamento interpessoal. Hoje cuido "
        "de dados comerciais, painéis de Power BI e automações de processos.",
    ],
    "foto": "portfolio/img/foto.jpg",
    "foto_alt": "Foto de Jônatas Marques de Farias",
    # Arquivo do currículo (dentro de portfolio/static/) e nome que aparece ao baixar.
    "curriculo_arquivo": "portfolio/docs/curriculo-jonatas-marques-de-farias.pdf",
    "curriculo_download": "Curriculo-Jonatas-Marques-de-Farias.pdf",
    "curriculo_info": "2 páginas · PDF",
}

# Faixa de resumo logo abaixo da apresentação: (rótulo, valor)
FICHA = [
    ("Atuação atual", "Analista Comercial com foco em dados, Santillana Educação"),
    ("Formação", "Ciência de Dados, UNIVESP (2023 a 2027, conclusão em jun/2027)"),
    ("Fontes de dados", "CRM Microsoft Dynamics, ERP TOTVS, Excel e Power Query"),
    ("Visualização e automação", "Power BI, Power Automate e Python"),
]

# ---------------------------------------------------------------------------
# Trajetória profissional (do mais recente para o mais antigo)
# ---------------------------------------------------------------------------
TRAJETORIA = [
    {
        "quando": "2022 até hoje",
        "atual": True,
        "titulo": "Analista Comercial com foco em dados",
        "org": "Santillana Educação",
        "itens": [
            "Atua no Núcleo de Apoio às Vendas, com coleta, gerenciamento e apresentação de dados "
            "voltados à inteligência de mercado e à criação de estratégias comerciais.",
            "Cria e acompanha dashboards para dar visibilidade clara e objetiva ao time comercial.",
            "Trabalha com dados do CRM (Microsoft Dynamics) e do ERP (TOTVS), com tratamento em Excel "
            "e Power Query e análises em Power BI e PowerPoint.",
            "Automatiza processos antes manuais com Power Automate, Python e integração com IA (Copilot).",
        ],
    },
    {
        "quando": "2020 a 2022",
        "atual": False,
        "titulo": "Analista Administrativo Júnior",
        "org": "UPS Group Brasil",
        "itens": [
            "Suporte ao time comercial, com carteirização dos consultores no CRM da empresa.",
            "Criação de relatórios gerenciais em Excel para acompanhar a performance.",
        ],
    },
    {
        "quando": "2017 a 2020",
        "atual": False,
        "titulo": "Analista de Atendimento em Turismo Pleno",
        "org": "Decolar",
        "itens": [
            "Suporte operacional a parceiros B2B (agências afiliadas).",
            "Gestão de incidentes com companhias aéreas, hotéis e demais provedores, nacionais e internacionais.",
            "Consultas, alterações e cancelamentos de reservas em sistemas GDS (Sabre) e portais de companhias aéreas.",
            "Treinamento e adaptação de novos funcionários e trabalho com os times comercial e operacional.",
        ],
    },
]

# ---------------------------------------------------------------------------
# Formação e cursos
# ---------------------------------------------------------------------------
FORMACAO = {
    "quando": "2023 a 2027",
    "titulo": "Ciência de Dados",
    "org": "UNIVESP, conclusão prevista em jun/2027",
}

# (curso, instituição)
CURSOS = [
    ("Excel Avançado", "Conquer"),
    ("Análise de dados com Power BI", "Conquer"),
    ("SQL: A Linguagem dos Bancos de Dados", "Conquer"),
    ("Microsoft Power BI para Business Intelligence", "Data Science Academy"),
    ("Inteligência Artificial para todos", "Hashtag Treinamentos"),
]

# ---------------------------------------------------------------------------
# Habilidades
# ---------------------------------------------------------------------------
FERRAMENTAS = [
    ("Power BI", "Relatórios e dashboards interativos, com dados tratados no Power Query."),
    ("Excel", "Tratamento de dados e relatórios gerenciais."),
    ("SQL", "Consulta e análise de dados em bancos de dados."),
    ("Python", "ETL e automação de processos, além de apps com Streamlit e Plotly."),
    ("Power Automate", "Automação de processos antes manuais, com apoio de IA (Copilot)."),
]

COMPETENCIAS = [
    "Análise de dados",
    "Inteligência de mercado",
    "Inteligência artificial",
    "Comunicação clara",
    "Relacionamento interpessoal",
]

# ---------------------------------------------------------------------------
# Projetos
# ---------------------------------------------------------------------------
# ferramenta: "power-bi", "python" ou "excel" (define o filtro).
# url: link público do projeto. Vazio mostra "Link em breve".
#      Para Power BI, cole o link de "Publicar na Web" (https://app.powerbi.com/view?r=...).
#      Também vale colar o código <iframe ...> inteiro: o site pega o endereço sozinho.
# incorporar: True mostra o botão "Ver painel aqui", que abre o painel em uma janela
#      dentro do site. Só funciona com links do app.powerbi.com. Sem url, nada aparece.
# pendente: True mostra o cartão tracejado, para projetos ainda por vir.
# slug, download, download_rotulo: oferecem um arquivo para baixar (veja o projeto de Excel abaixo).
FILTROS = [
    ("todos", "Todos"),
    ("power-bi", "Power BI"),
    ("python", "Python"),
    ("excel", "Excel"),
]

PROJETOS = [
    {
        "ferramenta": "power-bi",
        "stack": "Power BI",
        "titulo": "Dashboard de Marketing",
        "texto": "Relatório de 4 páginas sobre a base de clientes e as campanhas de marketing: perfil "
                 "dos clientes, resultado das campanhas, gasto por categoria e país, e a relação "
                 "entre salário, filhos em casa e gastos.",
        "visuais": ["4 páginas", "Compras por canal", "Resultado das campanhas", "Gasto por categoria e país", "Salário x gastos", "Árvore de decomposição"],
        "meta": "Arquivo: Dashboard_de_Marketing.pbix",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiNzg2Mzc4ZTItY2M5OS00ZWFmLWEwMzktZGYyYTk2YzBhNzNlIiwidCI6Ijc1MTZiYjE4LTI4MmMtNGU2My1iMWVjLTc5NTgwNWYxZThmZCIsImMiOjh9",
        "incorporar": True,
    },
    {
        "ferramenta": "power-bi",
        "stack": "Power BI",
        "titulo": "Análise de dados de RH",
        "texto": "Painel sobre o quadro de funcionários: total por função, divisão entre masculino e "
                 "feminino, salário médio, experiência média, envolvimento no trabalho e "
                 "disponibilidade para hora extra, com filtro por idade.",
        "visuais": ["Barras por função", "Rosca de envolvimento", "Pizza de hora extra", "Cartões de indicadores", "Filtro por idade"],
        "meta": "Arquivo: BI_RH.pbix",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYjJmODg0MTgtODZiYi00NWQ5LWIyYjUtOWJjODQyMjhhYWM4IiwidCI6Ijc1MTZiYjE4LTI4MmMtNGU2My1iMWVjLTc5NTgwNWYxZThmZCIsImMiOjh9",
        "incorporar": True,
    },
    {
        "ferramenta": "power-bi",
        "stack": "Power BI",
        "titulo": "Vendas por segmento, fabricante e estado",
        "texto": "Painel com valor total de venda, custo total e lucro, aberto por segmento, "
                 "fabricante, categoria e estado, com mapa e filtros de ano, vendedor, estado e cidade.",
        "visuais": ["Cartões de venda, custo e lucro", "Pizza por segmento", "Colunas por fabricante", "Funil por categoria", "Mapa por estado"],
        "meta": "Arquivo: BI_VENDAS.pbix",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM0OGE2NGUtMTBjOC00NzU4LTgxMGQtYzIzOTI3MzNmODlkIiwidCI6Ijc1MTZiYjE4LTI4MmMtNGU2My1iMWVjLTc5NTgwNWYxZThmZCIsImMiOjh9",
        "incorporar": True,
    },
    {
        "ferramenta": "python",
        "stack": "Python · Streamlit · Plotly",
        "titulo": "Mercado farmacêutico brasileiro em 2024",
        "texto": "Dashboard interativo sobre o mercado farmacêutico brasileiro, com base no Anuário "
                 "Estatístico CMED/ANVISA (ano-base 2024). Mostra faturamento, unidades vendidas, "
                 "empresas, produtos e princípios ativos, e compara quem fatura mais com quem vende "
                 "mais volume, por tipo de registro.",
        "visuais": ["Visão geral", "Canais de distribuição", "Faixas de preço", "Classes terapêuticas", "Princípios ativos", "Idade e composição", "Regime de preço (MIP x regulado)", "Empresas e concentração"],
        "meta": "Fonte: CMED/ANVISA, ano-base 2024",
        "url": "https://dashboard-app---ind-stria-farmac-utica-wz7sgfkpncaan3avwqizo6.streamlit.app/",
    },
    {
        "ferramenta": "excel",
        "stack": "Excel",
        "titulo": "Painel comercial: pipeline, metas e carteira",
        "texto": "Planilha de apoio ao time comercial: meta contra realizado por consultor, funil de "
                 "oportunidades com forecast ponderado, alertas de oportunidades paradas e de clientes "
                 "em risco. Usa dados fictícios.",
        "visuais": ["Painel com filtros", "3 gráficos", "Listas suspensas", "Fórmulas SUMIFS e INDEX/MATCH", "Alertas automáticos"],
        "meta": "Arquivo: Painel_Comercial_Pipeline_e_Metas.xlsx",
        "url": "",
        # Para oferecer um arquivo para baixar: ponha o arquivo em portfolio/static/portfolio/docs/
        # e preencha os três campos abaixo (o "slug" vira o endereço /baixar/<slug>/).
        "slug": "painel-comercial",
        "download": "portfolio/docs/Painel_Comercial_Pipeline_e_Metas.xlsx",
        "download_rotulo": "Baixar planilha (.xlsx)",
    },
]

# ---------------------------------------------------------------------------
# Contato (linhas com "valor" vazio não aparecem no site)
# ---------------------------------------------------------------------------
CONTATOS = [
    {"rotulo": "E-mail", "valor": "jonatasmfarias@gmail.com", "link": "mailto:jonatasmfarias@gmail.com", "copiar": True},
    {"rotulo": "Telefone", "valor": "(11) 96787-4348", "link": "tel:+5511967874348", "copiar": True},
    {"rotulo": "Cidade", "valor": "Guarulhos, SP", "link": "", "copiar": False},
    # Preencha quando quiser mostrar:
    {"rotulo": "LinkedIn", "valor": "", "link": "", "copiar": False},  # ex.: "linkedin.com/in/seu-perfil" e link "https://www.linkedin.com/in/seu-perfil"
    {"rotulo": "GitHub", "valor": "", "link": "", "copiar": False},    # ex.: "github.com/seu-usuario" e link "https://github.com/seu-usuario"
]
