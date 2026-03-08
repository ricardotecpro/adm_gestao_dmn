
# Gestão e Modelos de Negócios

Curso completo de Gestão e Modelos de Negócios para Análise e Desenvolvimento de Sistemas

## 🌐 Acesse o Site

👉 [Gestão e Modelos de Negócios](https://ricardotecpro.github.io/adm_gestao_dmn/)

## 🚀 Como Usar

### Pré-requisitos

- Python 3.11+
- Poetry
- Node.js 20+ (para reveal.js)

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/ricardotecpro/adm_gestao_dmn.git
cd adm_gestao_dmn

# Instalar dependências
poetry install

# Instalar dependências Node.js (reveal.js)
npm install

# Instalar navegadores para testes
poetry run playwright install chromium
```

### Desenvolvimento

```bash
# Servidor local com hot-reload
poetry run task serve

# Build do site
poetry run task build

# Gerar slides HTML
poetry run task slides

# Gerar quizzes interativos
poetry run task quizzes

# Rodar testes
poetry run task test

# Auditoria de conteúdo
poetry run task audit
```

## 📁 Estrutura

```
adm_gestao_dmn/
├── docs/                  # Conteúdo do curso (Markdown)
│   ├── aulas/            # Aulas organizadas por módulo
│   ├── slides/           # Slides em formato Reveal.js
│   ├── assets/           # CSS, JS, imagens
│   └── index.md          # Página inicial
├── hooks/                # Hooks do MkDocs
├── overrides/            # Templates customizados
├── scripts/              # Scripts de automação
├── tests/                # Testes automatizados
├── course.yml            # Configuração do curso
├── mkdocs.yml            # Configuração MkDocs (gerado)
├── pyproject.toml        # Dependências Poetry (gerado)
└── tasks.py              # Tarefas de automação
```

## 📋 Módulos

### Bloco 1 — Fundamentos de Gestão

- Aula 01 — Introdução à Gestão
- Aula 02 — Planejamento Estratégico
- Aula 03 — Processos de Negócio
- Aula 04 — Modelagem de Processos

### Bloco 2 — Modelos de Negócios

- Aula 05 — Business Model Canvas
- Aula 06 — Lean Canvas
- Aula 07 — Proposta de Valor
- Aula 08 — Análise de Mercado

### Bloco 3 — Gestão de Projetos

- Aula 09 — Metodologias Ágeis
- Aula 10 — Scrum e Kanban
- Aula 11 — Estimativas e Métricas
- Aula 12 — Qualidade e Riscos

### Bloco 4 — Tópicos Avançados

- Aula 13 — Governança de TI
- Aula 14 — Inovação e Empreendedorismo
- Aula 15 — Transformação Digital
- Aula 16 — Projeto Final



## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Feito com ❤️ usando [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
