import mimetypes
import os
import re
from datetime import date
from urllib.parse import urlparse

from django.contrib.staticfiles import finders
from django.http import FileResponse, Http404
from django.shortcuts import render

from . import content

# Só esses endereços podem aparecer dentro da janela do painel.
HOSTS_PERMITIDOS_NA_JANELA = {"app.powerbi.com", "app.fabric.microsoft.com"}


def _limpar_url(valor):
    """Aceita o link puro ou o código <iframe ...> inteiro copiado do Power BI."""
    valor = (valor or "").strip()
    achado = re.search(r"""src=["']([^"']+)["']""", valor)
    if achado:
        valor = achado.group(1)
    valor = valor.replace("&amp;", "&")
    return valor if valor.lower().startswith(("https://", "http://")) else ""


def _preparar_projeto(projeto):
    p = dict(projeto)
    p["url"] = _limpar_url(p.get("url"))
    host = urlparse(p["url"]).hostname if p["url"] else None
    p["incorporado"] = bool(p.get("incorporar")) and p["url"].startswith("https://") and host in HOSTS_PERMITIDOS_NA_JANELA
    return p


def _contexto_base(ativa):
    return {"pessoa": content.PESSOA, "ativa": ativa, "ano": date.today().year}


def perfil(request):
    chaves = {chave for chave, _ in content.FILTROS}
    filtro = request.GET.get("ferramenta", "todos")
    if filtro not in chaves:
        filtro = "todos"

    projetos = [
        _preparar_projeto(p) for p in content.PROJETOS if filtro == "todos" or p["ferramenta"] == filtro
    ]

    contexto = _contexto_base("perfil")
    contexto.update(
        {
            "ficha": content.FICHA,
            "trajetoria": content.TRAJETORIA,
            "formacao": content.FORMACAO,
            "cursos": content.CURSOS,
            "ferramentas": content.FERRAMENTAS,
            "competencias": content.COMPETENCIAS,
            "filtros": content.FILTROS,
            "filtro_ativo": filtro,
            "projetos": projetos,
        }
    )
    return render(request, "portfolio/perfil.html", contexto)


def contato(request):
    contexto = _contexto_base("contato")
    contexto["contatos"] = [c for c in content.CONTATOS if c["valor"]]
    return render(request, "portfolio/contato.html", contexto)


def baixar(request, slug):
    """Baixa o arquivo de um projeto. Só entrega arquivos declarados em content.PROJETOS."""
    projeto = next((p for p in content.PROJETOS if p.get("slug") == slug and p.get("download")), None)
    if projeto is None:
        raise Http404("Arquivo não encontrado.")
    caminho = finders.find(projeto["download"])
    if not caminho:
        raise Http404("Arquivo não encontrado.")
    nome = os.path.basename(projeto["download"])
    tipo = mimetypes.guess_type(nome)[0] or "application/octet-stream"
    return FileResponse(open(caminho, "rb"), as_attachment=True, filename=nome, content_type=tipo)


def curriculo(request):
    """Baixa o PDF do currículo (o arquivo fica em portfolio/static/portfolio/docs/)."""
    caminho = finders.find(content.PESSOA["curriculo_arquivo"])
    if not caminho:
        raise Http404("Currículo não encontrado.")
    return FileResponse(
        open(caminho, "rb"),
        as_attachment=True,
        filename=content.PESSOA["curriculo_download"],
        content_type="application/pdf",
    )


def handler404(request, exception=None):
    return render(request, "portfolio/404.html", status=404)
