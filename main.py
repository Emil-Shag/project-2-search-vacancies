from src.api import HhRu

if __name__ == "__main__":

    api = HhRu()
    vacancies = api.get_vacancies("Python")

    print(f"Найдено вакансий: {len(vacancies)}")

    for v in vacancies[:5]:
        salary = v.get("salary") or {}
        print(
            v.get("name"),
            salary.get("from"),
            salary.get("to"),
            v.get("alternate_url")
        )