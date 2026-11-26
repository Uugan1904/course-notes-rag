from course_notes_rag import __version__
from course_notes_rag.config import get_api_key


def test_version_is_set():
    assert __version__ == "0.1.0"


def test_missing_api_key_returns_none(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setattr("course_notes_rag.config.os.environ", {})
    assert get_api_key() is None
