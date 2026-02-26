import pytest
import os
from pathlib import Path


def test_content_structure_exists():
    """Verify that the basic directory structure exists."""
    assert Path("docs").exists(), "Docs directory missing"
    assert Path("docs/slides").exists(), "Slides directory missing"
    assert Path("docs/quizzes").exists(), "Quizzes directory missing"
    assert Path("docs/exercicios").exists(), "Exercises directory missing"
    assert Path("docs/projetos").exists(), "Projects directory missing"


def test_lessons_completeness():
    """Verify that lessons follow the naming convention and have content."""
    lessons = list(Path("docs/aulas").glob("aula-*.md"))
    assert len(lessons) > 0, "No lessons found in docs/aulas"
    for lesson in lessons:
        assert lesson.stat().st_size > 50, f"Lesson {lesson.name} is too small"


def test_slides_sync():
    """Verify that every lesson has a corresponding slide."""
    lessons = {f.stem for f in Path("docs/aulas").glob("aula-*.md")}
    slides = {f.stem for f in Path("docs/slides").glob("slide-*.md")}
    
    # Compare stem numbers
    lesson_nums = {re.search(r'\d+', l).group() for l in lessons if re.search(r'\d+', l)}
    slide_nums = {re.search(r'\d+', s).group() for s in slides if re.search(r'\d+', s)}
    
    missing = lesson_nums - slide_nums
    assert not missing, f"Lessons without slides: {missing}"


def test_quizzes_sync():
    """Verify that every lesson has a corresponding quiz."""
    lessons = {f.stem for f in Path("docs/aulas").glob("aula-*.md")}
    quizzes = {f.stem for f in Path("docs/quizzes").glob("quiz-*.md")}
    
    lesson_nums = {re.search(r'\d+', l).group() for l in lessons if re.search(r'\d+', l)}
    quiz_nums = {re.search(r'\d+', s).group() for s in quizzes if re.search(r'\d+', s)}
    
    missing = lesson_nums - quiz_nums
    assert not missing, f"Lessons without quizzes: {missing}"


def test_indexes_exist():
    """Verify that all subdirectory index files exist."""
    EXPECTED_INDEXES = [
        "aulas/index.md",
        "exercicios/index.md",
        "projetos/index.md",
        "quizzes/index.md",
        "slides/index.md",
        "setups/index.md"
    ]
    missing_indexes = []
    for index in EXPECTED_INDEXES:
        if not os.path.exists(f"docs/{index}"):
            missing_indexes.append(index)
    
    assert not missing_indexes, f"Missing indexes: {missing_indexes}"


import re # Ensure re is imported locally if used in helper or globally
