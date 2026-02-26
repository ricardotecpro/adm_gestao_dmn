import pytest
import re
import yaml
from pathlib import Path
from playwright.sync_api import Page, expect


def load_nav_config():
    """Loads navigation and site title from mkdocs.yml"""
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.UnsafeLoader)


class TestNavigation:
    """Agnostic navigation tests"""

    @pytest.fixture(autouse=True)
    def setup_config(self):
        self.config = load_nav_config()
        self.site_name = self.config.get("site_name", "Curso")
        self.nav = self.config.get("nav", [])

    def test_home_page_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página inicial carrega com o título correto"""
        page = page_with_base_url
        page.goto(base_url)
        expect(page).to_have_title(re.compile(rf"{self.site_name}"))

    def _ensure_menu_visible(self, page: Page):
        """Helper to ensure menu is visible (opens drawer if needed)"""
        drawer_button = page.locator("label.md-header__button[for='__drawer']")
        if drawer_button.is_visible() and not page.locator("nav.md-nav[aria-label='Menu']").is_visible():
            drawer_button.click()

    def test_navigation_menus_exist(self, page_with_base_url: Page, base_url: str):
        """Verifica se os menus principais definidos no nav do mkdocs.yml existem"""
        page = page_with_base_url
        page.goto(base_url)
        self._ensure_menu_visible(page)
        
        for item in self.nav:
            # item is a dict like {'Aulas': [...]} or {'Sobre': 'sobre.md'}
            menu_name = list(item.keys())[0]
            link = page.get_by_role("link", name=menu_name).first
            # Some items might be collapsible labels, not direct links
            # We just check if the text is present in the primary nav container
            expect(page.locator("nav.md-nav--primary")).to_contain_text(menu_name[:10])

    def test_navigation_to_first_lesson(self, page_with_base_url: Page, base_url: str):
        """Dinamicamente navega para a primeira aula encontrada no nav"""
        page = page_with_base_url
        page.goto(base_url)
        self._ensure_menu_visible(page)

        # Buscar seção de Aulas ou similar (geralmente o segundo item ou o que contém arquivos de aula)
        aulas_item = None
        for item in self.nav:
            name = list(item.keys())[0]
            if "Aula" in name or "Lição" in name:
                aulas_item = item
                break
        
        if not aulas_item:
            # Fallback to the second item if names don't match
            if len(self.nav) > 1:
                aulas_item = self.nav[1]
            else:
                pytest.skip("Aulas section not found in nav")

        aulas_section_name = list(aulas_item.keys())[0]
        aulas_list = aulas_item[aulas_section_name]
        
        # Encontrar primeiro módulo (aninhamento) ou primeira aula direta
        first_lesson_info = None
        module_name = None
        
        for item in aulas_list:
            if isinstance(item, dict):
                m_name = list(item.keys())[0]
                m_content = item[m_name]
                if isinstance(m_content, list) and len(m_content) > 0:
                    module_name = m_name
                    first_lesson_info = m_content[0]
                    break
            elif isinstance(item, str):
                # Caso a primeira "aula" seja o index.md ou similar
                continue

        if not first_lesson_info:
            pytest.skip("No lessons found in Aulas section")

        lesson_name = list(first_lesson_info.keys())[0] if isinstance(first_lesson_info, dict) else str(first_lesson_info)
        
        # Ação: Clicar na seção pai
        page.get_by_role("link", name=aulas_section_name).first.click(force=True)
        
        # Ação: Clicar no Módulo (se houver)
        if module_name:
            # Usa regex para ser resiliente a problemas de encoding com acentos (Módulo vs Módulo)
            safe_module_name = re.sub(r'[^a-zA-Z0-9\s]', '.', module_name)
            page.get_by_text(re.compile(rf"{safe_module_name}", re.IGNORECASE)).first.click(force=True)
            page.wait_for_timeout(500)
        
        # Ação: Clicar na Aula
        safe_lesson_name = re.sub(r'[^a-zA-Z0-9\s]', '.', lesson_name)
        lesson_link = page.get_by_role("link", name=re.compile(rf"{safe_lesson_name}", re.IGNORECASE), exact=False).first
        expect(lesson_link).to_be_visible()
        lesson_link.click(force=True)
        
        # Verificar chegada
        expect(page.locator("h1")).to_be_visible()
        expect(page.locator("h1")).to_contain_text(re.compile(r".*\d+"))
