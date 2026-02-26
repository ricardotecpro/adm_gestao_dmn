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

        # Find "Aulas" or similar section
        aulas_item = next((item for item in self.nav if "Aulas" in item), None)
        if not aulas_item:
            pytest.skip("Aulas section not found in nav")

        aulas_list = aulas_item["Aulas"]
        # Find first module (nesting)
        first_module = next((item for item in aulas_list if isinstance(item, dict)), None)
        if not first_module:
            pytest.skip("No modules found in Aulas")

        module_name = list(first_module.keys())[0]
        first_lesson_list = first_module[module_name]
        
        # Get first lesson link info
        first_lesson = first_lesson_list[0]
        lesson_name = list(first_lesson.keys())[0]
        
        # Action: Click Aulas
        page.get_by_role("link", name="Aulas").first.click(force=True)
        
        # Action: Click Module
        page.locator(f"label:has-text('{module_name}')").first.click(force=True)
        page.wait_for_timeout(500)
        
        # Action: Click Lesson
        lesson_link = page.get_by_role("link", name=lesson_name, exact=False).first
        expect(lesson_link).to_be_visible()
        lesson_link.click(force=True)
        
        # Verify arrival
        expect(page.locator("h1")).to_be_visible()
        # Header starts with "Aula XX"
        expect(page.locator("h1")).to_contain_text(re.compile(r"Aula \d+"))
