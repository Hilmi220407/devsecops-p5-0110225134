from app.models import Task
from app.utils import validate_title, count_done


def test_validate_title_valid():
    assert validate_title("Kerjakan tugas") is True


def test_validate_title_empty():
    assert validate_title("   ") is False


def test_validate_title_too_long():
    assert validate_title("a" * 101) is False


def test_count_done():
    a, b = Task(1, "A"), Task(2, "B")
    b.mark_done()
    assert count_done([a, b]) == 1