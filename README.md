# Portfólio de Jônatas Farias (Django)

Site de duas páginas: **Perfil e projetos** e **Contato e currículo**. Todo o texto fica em um único arquivo Python, então dá para editar direto no VS Code sem mexer em HTML.

## Rodar no VS Code (Windows)

1. Abra esta pasta no VS Code (`Arquivo > Abrir Pasta`).
2. Abra o terminal (`Ctrl + '`) e rode:

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

3. Acesse http://127.0.0.1:8000. Ao salvar um arquivo, o servidor recarrega sozinho; basta atualizar o navegador.

No macOS/Linux, troque a ativação por `source .venv/bin/activate`.

Para depurar, use `F5` (já existe a configuração "Django: runserver" em `.vscode/launch.json`).

## Onde editar

| O que mudar | Onde |
|---|---|
| Textos, trajetória, ferramentas, cursos, contatos | `portfolio/content.py` |
| Adicionar ou mudar um projeto | lista `PROJETOS` em `portfolio/content.py` |
| Foto | `portfolio/static/portfolio/img/foto.jpg` (troque o arquivo, mantendo o nome) |
| Currículo em PDF | `portfolio/static/portfolio/docs/` (e o nome em `PESSOA["curriculo_arquivo"]`) |
| Cores e fontes | variáveis no topo de `portfolio/static/portfolio/css/style.css` |
| Estrutura das páginas | `portfolio/templates/portfolio/` |

### Adicionar um projeto

Copie um bloco de `PROJETOS`, ajuste os campos e salve:

```python
{
    "ferramenta": "power-bi",          # power-bi, python ou excel (define o filtro)
    "stack": "Power BI",
    "titulo": "Nome do projeto",
    "texto": "O que o projeto mostra, em uma ou duas frases.",
    "visuais": ["Gráfico de barras", "Filtro por ano"],   # pode ser []
    "meta": "Arquivo: nome.pbix",
    "url": "https://app.powerbi.com/view?r=...",          # vazio = "Link em breve"
    "incorporar": True,                                   # True = botão "Ver painel aqui" (só Power BI)
},
```

### Mostrar o painel do Power BI dentro do site

1. No Power BI Service, abra o relatório e vá em `Arquivo > Inserir relatório > Publicar na Web (público)`.
2. Copie o link (ou o código `<iframe ...>` inteiro) e cole no campo `url` do projeto.
3. Confira que o projeto tem `"incorporar": True`. Os três projetos de Power BI já vêm assim.

Com isso o cartão ganha o botão **Ver painel aqui**, que abre o painel interativo em uma janela dentro do site, mais o botão **Abrir em nova aba**. Com `"incorporar": False` (ou sem a linha) aparece só o botão **Abrir projeto**, que abre o link em outra aba.

A janela só aceita endereços do `app.powerbi.com` (e `app.fabric.microsoft.com`). Qualquer outro endereço abre só em nova aba.

Atenção: "Publicar na Web" deixa o relatório e os dados **públicos para qualquer pessoa com o link**. Use só com dados que possam ser públicos. O projeto de RH tem salários, então confirme que a base é fictícia ou anonimizada antes de publicar. Em algumas contas de empresa o administrador desliga a opção "Publicar na Web".

### Oferecer um arquivo para baixar (planilha, PDF, etc.)

1. Coloque o arquivo em `portfolio/static/portfolio/docs/`.
2. No projeto, em `portfolio/content.py`, preencha três campos:

```python
"slug": "painel-comercial",                                   # vira o endereço /baixar/painel-comercial/
"download": "portfolio/docs/Painel_Comercial_Pipeline_e_Metas.xlsx",
"download_rotulo": "Baixar planilha (.xlsx)",                 # texto do botão (opcional)
```

O cartão ganha o botão de download e o navegador baixa o arquivo com o nome original. A rota `/baixar/<slug>/` só entrega arquivos cadastrados em `PROJETOS`, então nenhum outro arquivo do servidor fica exposto. Funciona para qualquer formato (`.xlsx`, `.pdf`, `.pbix`, `.zip`). O projeto de Excel já vem configurado assim.

Para trocar a planilha, substitua o arquivo mantendo o mesmo nome (ou mude o nome também em `download`).

## Testes

```powershell
python manage.py test
```

## Publicar na Vercel

1. Importe este repositório (`JonatasMF/Portifolio_2026`) em [vercel.com/new](https://vercel.com/new).
2. Mantenha a pasta raiz do projeto como diretório raiz. O `vercel.json` já configura o build dos arquivos estáticos e a função Django.
3. Nas configurações do projeto na Vercel, adicione as variáveis de ambiente:

```
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=<uma chave longa e aleatória>
```

A Vercel fornece automaticamente os endereços de preview e produção. Se usar um domínio próprio, inclua-o em `DJANGO_ALLOWED_HOSTS` (separe vários hosts por vírgula). Depois do primeiro deploy, novos pushes para o GitHub geram novos deploys automaticamente.

O site não usa banco de dados. WhiteNoise serve os arquivos estáticos incluídos na função; os arquivos de currículo e projetos continuam disponíveis pelas rotas existentes.
