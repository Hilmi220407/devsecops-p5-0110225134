from app.models import Task


def test_task_default_not_done():
    t = Task(1, "Belajar DevSecOps")
    assert t.done is False


def test_mark_done():
    t = Task(1, "Belajar DevSecOps")
    t.mark_done()
    assert t.done is True


def test_to_dict():
    t = Task(1, "Tes")
    assert t.to_dict() == {"id": 1, "title": "Tes", "done": False}