from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse

from . import content


class PaginasTests(SimpleTestCase):
    def test_perfil_mostra_nome_e_projetos(self):
        r = self.client.get(reverse("perfil"))
        self.assertContains(r, content.PESSOA["nome"])
        self.assertContains(r, "Análise de dados de RH")
        self.assertContains(r, "foto.jpg")

    def test_filtro_power_bi_esconde_python(self):
        r = self.client.get(reverse("perfil"), {"ferramenta": "power-bi"})
        self.assertContains(r, "Análise de dados de RH")
        self.assertNotContains(r, "Mercado farmacêutico brasileiro em 2024")

    def test_filtro_python_esconde_power_bi(self):
        r = self.client.get(reverse("perfil"), {"ferramenta": "python"})
        self.assertContains(r, "Mercado farmacêutico brasileiro em 2024")
        self.assertNotContains(r, "Análise de dados de RH")

    def test_filtro_invalido_mostra_todos(self):
        r = self.client.get(reverse("perfil"), {"ferramenta": "qualquer-coisa"})
        self.assertContains(r, "Análise de dados de RH")
        self.assertContains(r, "Mercado farmacêutico brasileiro em 2024")

    def test_contato_mostra_somente_linhas_preenchidas(self):
        r = self.client.get(reverse("contato"))
        self.assertContains(r, "jonatasmfarias@gmail.com")
        self.assertNotContains(r, "GitHub")

    def test_download_do_curriculo(self):
        r = self.client.get(reverse("curriculo"))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r["Content-Type"], "application/pdf")
        self.assertIn("attachment", r["Content-Disposition"])
        self.assertTrue(b"".join(r.streaming_content).startswith(b"%PDF"))


def _projeto(**extra):
    base = {
        "ferramenta": "power-bi",
        "stack": "Power BI",
        "titulo": "Painel de teste",
        "texto": "Texto.",
        "visuais": [],
        "meta": "",
        "url": "",
    }
    base.update(extra)
    return [base]


class PainelIncorporadoTests(SimpleTestCase):
    def _get(self, projetos):
        with patch.object(content, "PROJETOS", projetos):
            return self.client.get(reverse("perfil"))

    def test_link_powerbi_com_incorporar_mostra_botao_da_janela(self):
        r = self._get(_projeto(url="https://app.powerbi.com/view?r=ABC123", incorporar=True))
        self.assertContains(r, "Ver painel aqui")
        self.assertContains(r, 'data-painel-url="https://app.powerbi.com/view?r=ABC123"')
        self.assertContains(r, "Abrir em nova aba")

    def test_sem_incorporar_so_mostra_o_link(self):
        r = self._get(_projeto(url="https://app.powerbi.com/view?r=ABC123"))
        self.assertNotContains(r, "Ver painel aqui")
        self.assertContains(r, "Abrir projeto")

    def test_endereco_fora_do_powerbi_nao_abre_na_janela(self):
        r = self._get(_projeto(url="https://exemplo.com/painel", incorporar=True))
        self.assertNotContains(r, "Ver painel aqui")
        self.assertContains(r, "Abrir projeto")

    def test_aceita_codigo_iframe_colado(self):
        codigo = '<iframe title="RH" width="600" height="373" src="https://app.powerbi.com/view?r=XYZ&amp;pageName=1" frameborder="0" allowFullScreen="true"></iframe>'
        r = self._get(_projeto(url=codigo, incorporar=True))
        self.assertContains(r, 'data-painel-url="https://app.powerbi.com/view?r=XYZ&amp;pageName=1"')

    def test_sem_url_mostra_link_em_breve(self):
        r = self._get(_projeto(incorporar=True))
        self.assertContains(r, "Link em breve")
        self.assertNotContains(r, "Ver painel aqui")

    def test_endereco_com_esquema_perigoso_e_ignorado(self):
        r = self._get(_projeto(url="javascript:alert(1)", incorporar=True))
        self.assertNotContains(r, "javascript:")
        self.assertContains(r, "Link em breve")


class ProjetosDeBITests(SimpleTestCase):
    def test_filtro_power_bi_mostra_os_tres_projetos_de_bi(self):
        r = self.client.get(reverse("perfil"), {"ferramenta": "power-bi"})
        self.assertContains(r, "Dashboard de Marketing")
        self.assertContains(r, "Vendas por segmento, fabricante e estado")
        self.assertContains(r, "Análise de dados de RH")
        self.assertContains(r, 'class="card"', count=3)
        self.assertNotContains(r, "Dash_Cap03")


class DownloadDeProjetoTests(SimpleTestCase):
    def test_cartao_de_excel_mostra_botao_de_download(self):
        r = self.client.get(reverse("perfil"), {"ferramenta": "excel"})
        self.assertContains(r, "Baixar planilha")
        self.assertContains(r, reverse("baixar", args=["painel-comercial"]))
        self.assertNotContains(r, "Link em breve")

    def test_baixa_o_xlsx_como_anexo(self):
        r = self.client.get(reverse("baixar", args=["painel-comercial"]))
        self.assertEqual(r.status_code, 200)
        self.assertIn("attachment", r["Content-Disposition"])
        self.assertIn("Painel_Comercial_Pipeline_e_Metas.xlsx", r["Content-Disposition"])
        self.assertIn("spreadsheetml", r["Content-Type"])
        self.assertTrue(b"".join(r.streaming_content).startswith(b"PK"))

    def test_slug_desconhecido_da_404(self):
        self.assertEqual(self.client.get("/baixar/nao-existe/").status_code, 404)

    def test_nao_entrega_arquivo_fora_da_lista(self):
        # só slugs declarados em content.PROJETOS funcionam; caminhos não passam pela rota
        self.assertEqual(self.client.get("/baixar/..%2F..%2Fsettings/").status_code, 404)
        self.assertEqual(self.client.get("/baixar/curriculo/").status_code, 404)
