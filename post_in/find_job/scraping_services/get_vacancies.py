from .dev_by import dev_by_parsing
from .rabota_by import rabota_by_parsing


def get_vacancies(**kwargs) -> list:
    vacancies = []
    vacancies.extend(dev_by_parsing(**kwargs))
    vacancies.extend(rabota_by_parsing(**kwargs))
    return vacancies

