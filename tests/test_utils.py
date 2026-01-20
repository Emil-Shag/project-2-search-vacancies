from unittest.mock import patch

from src.utils import user_interface
from src.vacancies import Vacancy

sample_vacancies = [
    Vacancy(title="Python Dev", url="1", salary_from=100000, salary_to=150000, description="Опыт Python"),
    Vacancy(title="JS Dev", url="2", salary_from=90000, salary_to=120000, description="Опыт JS"),
]


def test_user_interface_search_and_top(monkeypatch):
    inputs = iter(["1", "python", "2", "", "2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: None)

    with patch("src.utils.HhRu.get_vacancies", return_value=sample_vacancies):
        with patch("src.utils.JsonFiles.add_vacancies") as mock_add:
            user_interface()

            assert mock_add.called


def test_user_interface_filter_keyword(monkeypatch):
    inputs = iter(["1", "python", "2", "python", "2"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: None)

    with patch("src.utils.HhRu.get_vacancies", return_value=sample_vacancies):
        with patch("src.utils.JsonFiles.add_vacancies"):
            user_interface()


def test_user_interface_exit(monkeypatch):
    inputs = iter(["2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: None)
    user_interface()


def test_user_interface_empty_query(monkeypatch):
    inputs = iter(["1", "", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: None)
    user_interface()


def test_user_interface_api_error(monkeypatch):
    inputs = iter(["1", "python", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: None)

    with patch("src.utils.HhRu.get_vacancies", side_effect=Exception("API error")):
        user_interface()
