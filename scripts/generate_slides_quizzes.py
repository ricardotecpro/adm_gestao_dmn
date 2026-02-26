import pathlib
import re
import sys
import io

# Fix for Windows encoding issues with emojis
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from rich import print
from rich.progress import track


def generate_slide_html(lesson_number: int) -> str:
    """Gera HTML para um slide específico"""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula {lesson_number:02d} - Desenvolvimento de Modelos de Negócios</title>
    
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/theme/black.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/monokai.css">
    <link rel="stylesheet" href="../assets/css/reveal-custom.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="slide-{lesson_number:02d}.md"
                     data-separator="^\\n---\\n$"
                     data-separator-vertical="^\\n--\\n$">
            </section>
        </div>
    </div>
    
    <style>
        .reveal .slide-number {{
            background-color: var(--r-controls-color, #42affa) !important;
            color: #ffffff !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 4px !important;
            padding: 4px 8px !important;
            bottom: 20px !important;
            left: 20px !important;
            right: auto !important;
            box-shadow: none !important;
        }}
    </style>

    <script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/markdown/markdown.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/math/math.js"></script>
    <script src="https://unpkg.com/mermaid@11.12.3/dist/mermaid.min.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            controls: true,
            progress: true,
            transition: 'slide',
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealMath.MathJax3 ],
            mathjax3: {{
                mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
                tex: {{
                    inlineMath: [ [ '$', '$' ], [ '\\\\(', '\\\\)' ] ]
                }}
            }}
        }}).then(() => {{
            document.querySelectorAll('pre code.language-mermaid').forEach(code => {{
                const pre = code.parentElement;
                const div = document.createElement('div');
                div.className = 'mermaid';
                div.textContent = code.textContent;
                pre.replaceWith(div);
            }});
            mermaid.initialize({{ startOnLoad: false, theme: 'dark' }});
            mermaid.run({{ querySelector: '.mermaid' }});
        }});
    </script>
</body>
</html>
'''


def convert_quiz_md_to_html(md_content: str) -> str:
    """Converte o formato MarkDown de quiz para o formato HTML interativo"""
    # Regex para capturar Perguntas, Opções e Explicações
    # 1. Título
    title_match = re.search(r'# (.*)', md_content)
    title = title_match.group(1) if title_match else "Quiz"
    
    html_output = [f"# {title}\n", '--8<-- "assets/quiz.html"\n']
    
    # Split by questions
    questions = re.split(r'\n\d+\. ', md_content)
    if not questions[0].strip().startswith('1.'):
        # The first element might be the title, discard it if it doesn't have a question
        questions = questions[1:]
    else:
        # If it starts with 1., the first split will have it
        questions[0] = questions[0].replace('1. ', '', 1)

    for i, q_block in enumerate(questions, 1):
        lines = q_block.strip().split('\n')
        if not lines: continue
        
        question_text = lines[0].strip()
        options = []
        explanation = ""
        
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('- ['):
                is_correct = 'x' in line.lower()[:5]
                option_text = line[line.find(']')+1:].strip()
                options.append((option_text, is_correct))
            elif line.startswith('*Explicação:'):
                explanation = line.replace('*Explicação:', '').strip('*').strip()
        
        # Build HTML
        html_output.append('<div class="quiz-container">')
        html_output.append(f'  <div class="quiz-question">{i}. {question_text}</div>')
        
        for opt_text, is_correct in options:
            correct_attr = "true" if is_correct else "false"
            feedback = f"✅ Correto! {explanation}" if is_correct else f"❌ Incorreto. {explanation}"
            html_output.append(f'  <div class="quiz-option" data-correct="{correct_attr}" data-feedback="{feedback}">{opt_text}</div>')
        
        html_output.append('  <div class="quiz-feedback"></div>')
        html_output.append('</div>\n')
        
    return "\n".join(html_output)


def generate_all_slides():
    """Gera arquivos HTML para todos os 16 slides"""
    slides_dst_dir = pathlib.Path('docs/slides')
    slides_src_dir = slides_dst_dir / 'src'
    
    if not slides_src_dir.exists():
        print("[yellow]⚠ Pasta docs/slides/src/ não encontrada.[/yellow]")
        return
    
    print("\n[bold cyan]📊 Gerando Slides HTML...[/bold cyan]")
    
    for i in track(range(1, 17), description="Processando slides..."):
        src_md_name = f"slide-{i:02d}.md"
        src_md_path = slides_src_dir / src_md_name
        dst_md_path = slides_dst_dir / src_md_name
        html_path = slides_dst_dir / f"slide-{i:02d}.html"
        
        if src_md_path.exists():
            content = src_md_path.read_text(encoding='utf-8')
            
            # 1. Corrigir fragmentos: transformar { .fragment } em <!-- .element: class="fragment" -->
            # Isso permite usar uma sintaxe mais limpa no source. Captura variações de espaço.
            content = re.sub(r'\{\s*\.fragment\s*\}', '<!-- .element: class="fragment" -->', content)
            
            # 1.1 Corrigir caminhos relativos: como o arquivo é copiado de docs/slides/src/ para docs/slides/,
            # os links que eram ../../area/item.md devem virar ../area/item.md
            content = re.sub(r'(\.\./){2}(exercicios|projetos|aulas)/', r'../\2/', content)
            
            # 2. Remover frontmatter (YAML) se existir, mas manter os comentários de slide do Reveal.js
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    # Se houver YAML no topo (comum em arquivos Markdown), removemos para não quebrar o Reveal.js
                    # Mas atenção: o split('---', 2) pode remover o primeiro slide se o arquivo começa com --- separador de slide
                    # No Reveal.js, slides costumam ser separados por ---. Se o arquivo começa com ---, ele pode ser YAML ou o primeiro slide.
                    # Vamos assumir que se começa com --- e termina com --- logo depois, é YAML.
                    header = parts[1]
                    if 'title:' in header or 'author:' in header:
                        content = parts[2].lstrip()
            
            dst_md_path.write_text(content, encoding='utf-8')
            html_path.write_text(generate_slide_html(i), encoding='utf-8')


def generate_all_quizzes():
    """Gera arquivos HTML para todos os 16 quizzes"""
    quizzes_dst_dir = pathlib.Path('docs/quizzes')
    quizzes_src_dir = quizzes_dst_dir / 'src'
    
    if not quizzes_src_dir.exists():
        print("[yellow]⚠ Pasta docs/quizzes/src/ não encontrada.[/yellow]")
        return
    
    print("\n[bold magenta]📝 Gerando Quizzes Interativos...[/bold magenta]")
    
    for i in track(range(1, 17), description="Processando quizzes..."):
        src_md_name = f"quiz-{i:02d}.md"
        src_md_path = quizzes_src_dir / src_md_name
        dst_md_path = quizzes_dst_dir / src_md_name
        
        if src_md_path.exists():
            content = src_md_path.read_text(encoding='utf-8')
            html_quiz = convert_quiz_md_to_html(content)
            dst_md_path.write_text(html_quiz, encoding='utf-8')


def main():
    print("[bold]🚀 Automação de Conteúdo: Desenvolvimento de Modelos de Negócios[/bold]")
    print("=" * 50)
    
    generate_all_slides()
    generate_all_quizzes()
    
    print("\n[green]✅ Conteúdo de Slides e Quizzes gerado com sucesso![/green]")


if __name__ == '__main__':
    main()
