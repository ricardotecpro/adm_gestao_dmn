import pytest
import re
import yaml
from pathlib import Path
from playwright.sync_api import Page, expect


def load_config():
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.UnsafeLoader)


@pytest.fixture(scope="module")
def config():
    return load_config()


# Test 1: Verify build output files exist
def test_build_output_exists():
    """Verify that basic build output files exist."""
    assert Path("site/index.html").exists(), "Main index.html not found"
    # Lessons and other content existence checked in test_course_structure.py
    assert Path("site/assets/js/quiz.js").exists(), "Quiz JS not found"
    assert Path("site/assets/css/quiz.css").exists(), "Quiz CSS not found"


# Test 2: Homepage structure and content
def test_homepage_structure(page: Page, base_url, config):
    """Test that the homepage loads and has correct title from config."""
    site_name = config.get("site_name", "Curso")
    page.goto(base_url)
    expect(page).to_have_title(re.compile(rf"{site_name}"))
    expect(page.locator("h1")).to_contain_text(site_name)


# Test 3: Lesson pages load
def test_lesson_pages_accessible(page: Page, base_url):
    """Test that the first lesson page loads."""
    # Find first lesson file
    lesson_files = sorted(Path("docs/aulas").glob("aula-*.md"))
    if not lesson_files:
        pytest.skip("No lessons found")
    
    lesson_name = lesson_files[0].stem
    page.goto(f"{base_url}/aulas/{lesson_name}/")
    expect(page.locator("h1")).to_be_visible()


# Test 4: Quiz interactivity (Agnostic)
def test_quiz_functionality(page: Page, base_url):
    """Test that quiz JavaScript works correctly on the first quiz found."""
    quiz_files = sorted(Path("docs/quizzes").glob("quiz-*.md"))
    if not quiz_files:
        pytest.skip("No quizzes found")
        
    quiz_name = quiz_files[0].stem
    page.goto(f"{base_url}/quizzes/{quiz_name}/")
    
    first_quiz = page.locator(".quiz-container").first
    if first_quiz.is_visible():
        correct_option = first_quiz.locator(".quiz-option[data-correct='true']").first
        correct_option.click()
        feedback = first_quiz.locator(".quiz-feedback")
        expect(feedback).to_be_visible()
        expect(feedback).to_contain_text("Correto")


# Test 5: Infrastructure rendering
def test_renderers_present(page: Page, base_url):
    """Test standard renderers (Mermaid, MathJax) presence on a lesson page."""
    lesson_files = sorted(Path("docs/aulas").glob("aula-*.md"))
    if not lesson_files:
        pytest.skip("No lessons found")
        
    page.goto(f"{base_url}/aulas/{lesson_files[0].stem}/")
    # Just check if assets are attached
    expect(page.locator("script[src*='mermaid']").first).to_be_attached()

