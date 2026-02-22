# Aula 07 - Modelagem de Negócios: O Canvas 🧪

!!! tip "Objetivo"
    **Objetivo**: Dominar o Business Model Canvas (BMC), a ferramenta visual mais poderosa para projetar e analisar modelos de negócios, permitindo uma visão holística e ágil da estrutura da empresa.

---

## 1. O que é o Canvas? 🎨

O **Business Model Canvas** é um mapa visual que resume o modelo de negócio em 9 blocos fundamentais. Ele permite que você entenda como a empresa cria, entrega e captura valor em uma única página.

---

## 2. Os 9 Blocos do Canvas 🧱

Para modelar seu negócio, você deve preencher:

1.  **Segmento de Clientes**: Quem estamos atendendo?
2.  **Proposta de Valor**: Que problema resolvemos?
3.  **Canais**: Como chegamos ao cliente?
4.  **Relacionamento**: Como interagimos com cada segmento?
5.  **Fontes de Receita**: Como ganhamos dinheiro?
6.  **Recursos Principais**: O que é essencial para o negócio?
7.  **Atividades Principais**: O que fazemos no dia a dia?
8.  **Parcerias Principais**: Quem nos ajuda?
9.  **Estrutura de Custos**: O que gera gasto?

---

## 3. A Lógica do Canvas (Mermaid) 🔗

O Canvas é dividido em dois lados: o lado **Direito** (valor e cliente) e o lado **Esquerdo** (eficiência e infraestrutura).

```mermaid
graph TD
    subgraph "Lado Emocional (Valor)"
        V(["Proposta de Valor"]) --> C(["Canais"])
        C --> R(["Relacionamento"])
        R --> CL(["Segmentos de Clientes"])
        CL --> RE(["Receitas"])
    end
    subgraph "Lado Racional (Eficiência)"
        P(["Parcerias"]) --> A(["Atividades"])
        A --> RP(["Recursos"])
        RP --> CU(["Custos"])
    end
    V --- RP
    V --- A
```

---

## 4. Canvas vs. Plano de Negócios 📊

*   **Canvas**: Ágil, visual, focado em testes de hipóteses e mudanças rápidas.
*   **Plano de Negócios**: Detalhado, linear, focado em execução e captação de recursos tradicionais.

> **Dica**: Use o Canvas para encontrar o modelo certo e o Plano de Negócios para detalhar como você vai executá-lo.

---

## 5. Simulando um Modelo (Termynal) 📥

Vamos rodar uma verificação no seu Canvas:

```termynal
$ canvas --check-balance
> Verificando equilíbrio entre lados... [OK]
> Checando Proposta de Valor vs Cliente... [CONECTADO]
> Analisando Receitas vs Custos... [ALERTA: Margem Pequena]
> Diagnóstico: Seu modelo é viável, mas os custos operacionais estão altos!
```

---

## 6. Mini-Projeto: Modelando uma Startup 🏗️

Imagine que você está criando o **Uber das Bicicletas**.
1.  Qual a sua principal **Proposta de Valor**?
2.  Quem são seus **Segmentos de Clientes**?
3.  Quais seriam seus dois principais **Recursos**?
4.  De onde viria sua **Fonte de Receita**?

---

## 7. Exercício de Fixação 🧠

1.  Quais são los 9 blocos do Business Model Canvas?
2.  O que o "lado direito" do Canvas representa?
3.  Por que o Canvas é considerado uma ferramenta de "metodologia ágil"?

---

**Próxima Aula**: Como definir exatamente quem é seu cliente? [Segmentação de Clientes e Público-Alvo](./aula-08.md) 🚢
