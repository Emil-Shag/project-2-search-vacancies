import re
from typing import Optional, Tuple


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("__title", "__url", "__salary_from", "__salary_to", "__description")

    title: str
    url: str
    salary_from: int
    salary_to: int
    description: str

    def __init__(self, title, url, salary_from=None, salary_to=None, description="") -> None:
        """Инициализация вакансии с валидированием атрибутов"""
        self.__title = self.__validate_title(title)
        self.__url = self.__validate_url(url)
        self.__salary_from, self.__salary_to = self.__validate_salary(salary_from, salary_to)
        self.__description = self.__validate_description(description)

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнивает вакансии по минимальной зарплате"""
        return self.__salary_from < other.__salary_from

    @staticmethod
    def __validate_title(title: str) -> str:
        """Возвращает title или 'Название не указано', если пустой."""
        return str(title) if title else "Название не указано"

    @staticmethod
    def __validate_url(url: str) -> str:
        """Возвращает url или 'Ссылка не указана', если пустой."""
        return str(url) if url else "Ссылка не указана"

    @staticmethod
    def __validate_salary(salary_from: Optional[int], salary_to: Optional[int]) -> Tuple[int, int]:
        """Валидирует зарплату. Если salary_from или salary_to None, заменяет на 0."""
        salary_from = salary_from if salary_from is not None else 0
        salary_to = salary_to if salary_to is not None else 0
        return salary_from, salary_to

    @staticmethod
    def __validate_description(description: str) -> str:
        """Возвращает описание вакансии или 'Описание не указано', если пустое."""
        return re.sub(r"</?highlighttext>", "", description) if description else "Описание не указано"

    @property
    def title(self) -> str:
        """Возвращает заголовок"""
        return self.__title

    @property
    def url(self) -> str:
        """Возвращает заголовок"""
        return self.__url

    @property
    def salary_from(self) -> int:
        """Возвращает нижнюю границу зарплаты"""
        return self.__salary_from

    @property
    def salary_to(self) -> int:
        """Возвращает верхнюю границу зарплаты"""
        return self.__salary_to

    @property
    def description(self) -> str:
        """Возвращает описание"""
        return self.__description

    def __repr__(self) -> str:
        """Строковое представление объекта для отладки и печати."""
        return f"Vacancy(title={self.__title!r}, salary_from={self.__salary_from}, salary_to={self.__salary_to})"

    def to_dict(self) -> dict:
        """Конвертация объекта Vacancy в словарь для JSON"""
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }
