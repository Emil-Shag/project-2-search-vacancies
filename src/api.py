from abc import ABC, abstractmethod
import requests
from src.vacancies import Vacancy

class AbstractApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def connect_api(self):
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, vacancy_name):
        """Выдача списка вакансий по строке поиска"""
        pass

class HhRu(AbstractApi):
    """Класс для работы с hh.ru"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def connect_api(self):
        """Реализация абстрактного метода"""
        return self.__connect_api()

    def __connect_api(self):
        """Приватный метод подключения к API hh.ru"""
        response = requests.get(self.__base_url, headers=self.__headers)
        response.raise_for_status()
        return requests

    def get_vacancies(self, vacancy_name):
        """Получение вакансий по ключевому слову"""

        requests_obj = self.connect_api()

        params = {
            "text": vacancy_name,
            "per_page": 100
        }

        response = requests_obj.get(
            self.__base_url,
            headers=self.__headers,
            params=params
        )
        response.raise_for_status()

        data = response.json()["items"]

        vacancies = []
        for item in data:
            salary = item.get("salary") or {}
            vacancy = Vacancy(
                title=item.get("name"),
                url=item.get("alternate_url"),
                salary_from=salary.get("from"),
                salary_to=salary.get("to"),
                description=item.get("snippet", {}).get("requirement")
            )
            vacancies.append(vacancy)

        return vacancies