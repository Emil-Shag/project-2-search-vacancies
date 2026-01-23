from src.api import HhRu
from src.files import JsonFiles


def user_interface() -> None:

    hh = HhRu()
    storage = JsonFiles()

    print("Добро пожаловать в поиск вакансий hh.ru!")

    while True:
        print("\nВыберите действие:")
        print("1 — Найти вакансии")
        print("2 — Выйти из программы")

        choice = input("Ваш выбор: ").strip()

        if choice == "2":
            print("Программа завершена.")
            break

        if choice != "1":
            print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")
            continue

        query = input("\nВведите ключевое слово для поиска вакансий: ").strip()
        if not query:
            print("Поисковый запрос не может быть пустым.")
            continue

        try:
            vacancies = hh.get_vacancies(query)
        except Exception as e:
            print(f"Ошибка при подключении к API: {e}")
            continue

        if not vacancies:
            print("Вакансии не найдены.")
            continue

        storage.add_vacancies([v.to_dict() for v in vacancies])
        print(f"\nНайдено и сохранено {len(vacancies)} вакансий.")

        while True:
            try:
                n = int(input("Сколько вакансий показать по зарплате? "))
                if n <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Введите корректное положительное число.")

        top_vacancies = sorted(vacancies, reverse=True)[:n]

        print(f"\nТоп {n} вакансий по зарплате:")
        for i, v in enumerate(top_vacancies, 1):
            print(f"{i}. {v.title}")
            print(f"   Зарплата: от {v.salary_from} до {v.salary_to}")
            print(f"   Ссылка: {v.url}")
            print(f"   Описание: {v.description}\n")

        keyword = input("Введите ключевое слово для поиска в описании (Enter — пропустить): ").strip()
        if keyword:
            filtered = [v for v in vacancies if keyword.lower() in v.description.lower()]
            if filtered:
                print(f"\nНайдено вакансий: {len(filtered)}")
                for i, v in enumerate(filtered, 1):
                    print(f"{i}. {v.title}")
                    print(f"   Зарплата: от {v.salary_from} до {v.salary_to}")
                    print(f"   Ссылка: {v.url}")
                    print(f"   Описание: {v.description}\n")
            else:
                print("Совпадений в описании не найдено.")

        print("Поиск завершён.")
