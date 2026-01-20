
from unittest.mock import patch
from src.files import JsonFiles

vacancies_sample = [
    {"title": "Python Dev", "url": "1"},
    {"title": "JS Dev", "url": "2"},
]

def test_add_vacancies_with_mock():
    storage = JsonFiles(filename="dummy.json")

    with patch.object(storage, "_load_file", return_value=[]) as mock_load:

        with patch.object(storage, "_save_file") as mock_save:
            storage.add_vacancies(vacancies_sample)

            mock_load.assert_called_once()

            mock_save.assert_called_once_with(vacancies_sample)

def test_get_vacancies_with_criterion_mock():
    storage = JsonFiles(filename="dummy.json")

    with patch.object(storage, "_load_file", return_value=vacancies_sample):
        storage_data = storage.get_vacancies()
        assert len(storage_data) == 2

        filtered = storage.get_vacancies(criterion={"title": "Python Dev"})
        assert len(filtered) == 1
        assert filtered[0]["url"] == "1"

def test_remove_vacancy_mock():
    storage = JsonFiles(filename="dummy.json")

    with patch.object(storage, "_load_file", return_value=vacancies_sample):
        with patch.object(storage, "_save_file") as mock_save:
            storage.remove_vacancy({"url": "1"})

            mock_save.assert_called_once_with([{"title": "JS Dev", "url": "2"}])
