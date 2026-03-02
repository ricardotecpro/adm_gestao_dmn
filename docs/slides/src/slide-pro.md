<!-- .slide: class="center" -->

# 🏆 Padrão Ouro Pro 🚀

### Validação Exaustiva e Navegação 2D
[Seta Direita: Próximo Tópico | Seta Baixo: Detalhes]

---

## 1. Mídia e Diagramas 🏗️
(Siga para baixo para ver os testes)

--

### 1.1 Mermaid
<div class="mermaid">
graph TD
    A[Início] --> B{Decisão}
    B -- Sim --> C[Resultado A]
    B -- Não --> D[Resultado B]
    C --> E[Fim]
    D --> E
</div>

--

### 1.2 MathJax
A equação quadrática:
`$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$`

--

### 1.3 Termynal
<div id="termynal-pro" data-termynal>
    <span data-ty="input">mkdocs build --ignore-legado</span>
    <span data-ty="progress"></span>
    <span data-ty="exit">[OK] Build concluído!</span>
</div>

---

## 2. Material Features 💡
(Siga para baixo para ver Admonitions e Grids)

--

### 2.1 Admonitions (Estilizados)
<div class="admonition info">
    <p class="admonition-title">Dica Pro</p>
    <p>Use navegação vertical para detalhes técnicos sem poluir o fluxo principal.</p>
</div>

<div class="admonition success">
    <p class="admonition-title">Sucesso</p>
    <p>O teste de renderização foi integrado ao pipeline de build.</p>
</div>

--

### 2.2 Grid Cards
<div class="grid-cards-pro">
    <div class="card">
        <strong>Feature A</strong>
        <p>Alta performance com Reveal.js standalone.</p>
    </div>
    <div class="card">
        <strong>Feature B</strong>
        <p>Agnóstico a frameworks externos.</p>
    </div>
</div>

---

## 3. Comparativo de Imagens 🖼️
(Validando transparência e cores)

--

### 3.1 Prova de SVG (via PNG)
| P&B / Cinza | Colorido Transparente |
| :--- | :--- |
| ![BW](../assets/images/logo_test_bw.png) | ![Color](../assets/images/logo_test_color.png) |

--

### 3.2 Prova de Transparência
As imagens acima devem se integrar perfeitamente ao fundo escuro do slide.

---

## 4. Tabelas e Listas 📊

--

### 4.1 Tabelas Limpas
| Recurso | Status | Nota |
| :--- | :--- | :--- |
| Navegação 2D | ✅ | Horizontal/Vertical |
| Markdown | ✅ | Nativo |
| CSS Custom | ✅ | Injectado |

--

### 4.2 Listas com Fragmentos
- Item 1 <!-- .element: class="fragment" -->
- Item 2 <!-- .element: class="fragment" -->
- Item 3 <!-- .element: class="fragment" -->

---

<!-- .slide: class="center" -->
# FIM DO TESTE PRO
### 100% Padrão Ouro ✅
