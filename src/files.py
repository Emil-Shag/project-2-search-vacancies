import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class AbstractFiles(ABC):
    """Абстрактный класс для работы с файлами вакансий."""

    @abstractmethod
    def add_vacancies(self, vacancies: List[Dict]) -> None:
        """Добавляет вакансии в файл (список объектов или словарей)."""
        pass

    @abstractmethod
    def get_vacancies(self, criterion: Optional[Dict[str, str]] = None) -> List[dict]:
        """Получает данные из файла по заданным критериям."""
        pass

    @abstractmethod
    def remove_vacancy(self, criterion: Dict[str, str]) -> None:
        """Удаляет вакансии из файла, соответствующие критериям."""
        pass


class JsonFiles(AbstractFiles):
    """Класс для работы с вакансиями в JSON-файле."""

    filename: str

    def __init__(self, filename="vacancies.json") -> None:
        """Инициализация класса"""
        base_dir: str = os.path.dirname(os.path.dirname(__file__))
        data_dir: str = os.path.join(base_dir, "data")

        os.makedirs(data_dir, exist_ok=True)

        self.__filename = os.path.join(data_dir, filename)

    def add_vacancies(self, vacancies: List[dict]) -> None:
        """Добавляет вакансии в JSON-файл, избегая дублирования по URL."""
        existing = self._load_file()
        urls = {v["url"] for v in existing}
        for v in vacancies:
            if v["url"] not in urls:
                existing.append(v)
                urls.add(v["url"])

        self._save_file(existing)

    def get_vacancies(self, criterion: Optional[Dict[str, str]] = None) -> List[dict]:
        """Возвращает список вакансий, фильтруя по criterion."""
        data = self._load_file()
        if not criterion:
            return data

        result = []
        for v in data:
            match = True
            for key, value in criterion.items():
                if v.get(key) != value:
                    match = False
                    break
            if match:
                result.append(v)
        return result

    def remove_vacancy(self, criterion: Optional[Dict[str, str]]) -> Any:
        """Удаляет вакансии, соответствующие критериям."""
        data = self._load_file()
        filtered = [v for v in data if not all(v.get(k) == val for k, val in criterion.items())]
        self._save_file(filtered)

    def _load_file(self) -> Any:
        """Загружает данные из JSON-файла, если он существует."""
        if os.path.exists(self.__filename):
            with open(self.__filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save_file(self, data: List[dict]) -> None:
        """Сохраняет список вакансий в JSON-файл."""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
