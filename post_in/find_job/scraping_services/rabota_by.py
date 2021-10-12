# rabota.by

from find_job.scraping_services.site_access import get_site_page

cities = {
    "minsk": 1002,
    "brest": 1007,
    "vitebsk": 1005,
    "gomel": 1003,
    "grodno": 1006,
    "mogilev": 1004
}


def rabota_by_parsing(specialty: str, city: str) -> list:
    page_number = 0
    vacancies = []
    while True:
        domain = 'https://rabota.by/search/vacancy'
        params = {'text': f'{specialty}',
                  'area': cities[city],
                  'search_period': 30,   # за месяц
                  '&items_on_page': 100,   # по 100 на страницу
                  'page': page_number
                  }

        status, content = get_site_page(domain, params).values()
        if status != 200:
            return status
        next_button = content.find('a', attrs={'data-qa': 'pager-next'})

        blocks = content.find_all('div', attrs={
            'class': 'vacancy-serp-item',
        })
        for block in blocks:
            try:
                title = block.find('a', attrs={'class': 'bloko-link'}).text
                description_block = block.find_all('div', attrs={
                    'data-qa': ['vacancy-serp__vacancy_snippet_responsibility', 'vacancy-serp__vacancy_snippet_requirement']
                })
                description = ' '.join([a.text for a in description_block])
                company = block.find('a', attrs={
                    'data-qa': ['vacancy-serp__vacancy-employer']
                }).text
                url = block.a['href']
                vacancies.append({
                    'title': title,
                    'description': description,
                    'company': company,
                    'url': url,
                    'site': 'https://rabota.by/'
                })
            except AttributeError:
                pass
        if not next_button:
            return vacancies
        page_number += 1

