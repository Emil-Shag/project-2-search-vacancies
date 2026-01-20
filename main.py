from src.vacancies import Vacancy  # импорт класса Vacancy

if __name__ == "__main__":

    v1 = Vacancy("Python Developer", "https://hh.ru/vac1", 100000, 150000, "Разработка на Python")
    v2 = Vacancy("Java Developer", "https://hh.ru/vac2", 120000, 180000, "Разработка на Java")
    v3 = Vacancy("", "", None, None, "")  # пустые значения, проверяем валидацию

    print("Все вакансии:")
    print(v1)
    print(v2)
    print(v3)
    print()

    print("Проверка публичных свойств v3:")
    print(f"Title: {v3.title}")
    print(f"URL: {v3.url}")
    print(f"Salary from: {v3.salary_from}")
    print(f"Salary to: {v3.salary_to}")
    print(f"Description: {v3.description}")
    print()

    print("Сравнение вакансий по минимальной зарплате:")
    print(f"v1 < v2: {v1 < v2}")   # True
    print(f"v1 > v2: {v1 > v2}")   # False
    print(f"v1 == v3: {v1 == v3}") # False (v3.salary_from = 0)
    print()

    vacancies = [v1, v2, v3]
    sorted_vacancies = sorted(vacancies)  # использует __lt__
    print("Вакансии отсортированы по минимальной зарплате:")
    for v in sorted_vacancies:
        print(f"{v.title}: {v.salary_from} - {v.salary_to}")
