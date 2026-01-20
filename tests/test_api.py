from unittest.mock import patch, Mock
from src.api import HhRu


@patch("src.api.requests.get")
def test_connect_api_success(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    api = HhRu()
    api.connect_api()

    mock_get.assert_called_once()

@patch("src.api.requests.get")
def test_get_vacancies_returns_list(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": {"from": 100000, "to": 150000},
                "snippet": {"requirement": "Опыт Python"}
            }
        ]
    }

    mock_get.return_value = mock_response

    api = HhRu()
    vacancies = api.get_vacancies("python")

    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Developer"
    assert vacancies[0].salary_from == 100000

@patch("src.api.requests.get")
def test_get_vacancies_empty(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    api = HhRu()
    vacancies = api.get_vacancies("unknown")

    assert vacancies == []