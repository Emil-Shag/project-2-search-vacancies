from src.vacancies import Vacancy


def test_vacancy_repr():
    vacancy = Vacancy(
        title="Python Developer",
        url="https://example.com",
        salary_from=100000,
        salary_to=150000,
        description="Опыт работы с Python",
    )

    repr_str = repr(vacancy)

    assert "Python Developer" in repr_str
    assert "100000" in repr_str
    assert "150000" in repr_str
    assert isinstance(repr_str, str)
