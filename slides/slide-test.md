# Teste de Renderização: Materiais Interativos 🛠️

## Slide 1: Mermaid (DIRECT HTML)
<div class="mermaid">
graph LR
    A[Início] --> B{Decisão}
    B -- Sim --> C[Resultado A]
    B -- Não --> D[Resultado B]
    C --> E[Fim]
    D --> E
</div>

---

## Slide 2: MathJax (Bhaskara)
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

---

## Slide 3: Terminal Interativo (Termynal)

```termynal
$ mkdocs build
> Building documentation...
> Site built in 2.5 seconds
```

---

## Slide 4: Admonitions (Alertas)

!!! info "Informação"
    Este é um alerta de informação renderizado no slide.

!!! success "Sucesso"
    Operação concluída com êxito!

---

## Slide 5: Logotipo da Aula (DATA-URI)
<!-- Usando Data-URI para evitar qualquer stall de rede do servidor dev -->
<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDI1MCAxMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPHJlY3Qgd2lkdGg9IjI1MCIgaGVpZ2h0PSIxMDAiIGZpbGw9Im5vbmUiIC8+CiAgPHRleHQgeD0iNTAlIiB5PSI1MCUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSI0MCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IndoaXRlIj4KICAgIExPR08tU1ZHCiAgPC90ZXh0Pgo8L3N2Zz4=" width="250" alt="Logo Branco SVG">

---

## Slide 6: Logotipo da Aula (.png)
<!-- Usando caminho absoluto relativo à raiz do site para garantir resolução -->
<img src="/ads_gestao_dmn/assets/images/logo-test.png" width="250" alt="Logo Branco PNG">

---

<!-- .slide: class="center" -->
# FIM DO TESTE
[Voltar para Aulas](../aulas/index.md)
