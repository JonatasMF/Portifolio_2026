/* Botões "Copiar" da página de contato. Sem JavaScript, os contatos continuam clicáveis. */
document.addEventListener("click", function (e) {
  var botao = e.target.closest("[data-copiar]");
  if (!botao) return;
  var texto = botao.getAttribute("data-copiar");
  var original = botao.textContent;

  function avisar(msg) {
    botao.textContent = msg;
    setTimeout(function () { botao.textContent = original; }, 1600);
  }
  function selecionar() {
    var alvo = botao.parentNode.querySelector(".v");
    var faixa = document.createRange();
    faixa.selectNodeContents(alvo);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(faixa);
    avisar("Selecionado");
  }

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(texto).then(function () { avisar("Copiado"); }, selecionar);
  } else {
    selecionar();
  }
});

/* Janela do painel de Power BI: carrega o painel só quando o visitante abre. */
(function () {
  var janela = document.getElementById("painel");
  if (!janela) return;
  var quadro = document.getElementById("painel-quadro");
  var titulo = document.getElementById("painel-titulo");
  var link = document.getElementById("painel-link");

  document.addEventListener("click", function (e) {
    var botao = e.target.closest("[data-painel-url]");
    if (!botao) return;
    var url = botao.getAttribute("data-painel-url");
    if (typeof janela.showModal !== "function") {
      window.open(url, "_blank", "noopener");
      return;
    }
    titulo.textContent = botao.getAttribute("data-painel-titulo") || "Painel";
    quadro.title = "Painel: " + titulo.textContent;
    link.href = url;
    quadro.src = url;
    janela.showModal();
  });

  janela.addEventListener("close", function () { quadro.src = "about:blank"; });
  janela.addEventListener("click", function (e) { if (e.target === janela) janela.close(); });
})();
