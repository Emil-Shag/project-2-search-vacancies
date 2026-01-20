from abc import ABC, abstractmethod
from typing import List, Optional

import requests

from src.vacancies import Vacancy


class AbstractApi(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def connect_api(self) -> Optional[None]:
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, vacancy_name: str) -> List[Vacancy]:
        """Выдача списка вакансий по строке поиска"""
        pass


class HhRu(AbstractApi):
    """Класс для работы с hh.ru"""

    __base_url: str
    __headers: dict

    def __init__(self) -> None:
        """Инициализация класса"""
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def connect_api(self) -> None:
        """Реализация абстрактного метода"""
        return self.__connect_api()

    def __connect_api(self) -> None:
        """Приватный метод подключения к API hh.ru"""
        response = requests.get(self.__base_url, headers=self.__headers, params={"per_page": 1})
        response.raise_for_status()
        return None

    def get_vacancies(self, vacancy_name: str) -> List[Vacancy]:
        """Получение вакансий по ключевому слову"""

        self.connect_api()

        params: dict[str, str | int] = {"text": vacancy_name, "per_page": 100}
        response = requests.get(self.__base_url, headers=self.__headers, params=params)
        response.raise_for_status()

        data: list[dict] = response.json().get("items", [])
        vacancies: List[Vacancy] = []
        for item in data:
            salary = item.get("salary") or {}
            vacancy = Vacancy(
                title=item.get("name"),
                url=item.get("alternate_url"),
                salary_from=salary.get("from"),
                salary_to=salary.get("to"),
                description=item.get("snippet", {}).get("requirement"),
            )
            vacancies.append(vacancy)

        return vacancies
