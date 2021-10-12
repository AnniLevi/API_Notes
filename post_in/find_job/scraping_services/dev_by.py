# dev.by

from find_job.scraping_services.site_access import get_site_page


cities = {
    "minsk": 4429,
    "brest": 4316,
    "vitebsk": 4342,
    "gomel": 4372,
    "grodno": 4396,
    "mogilev": 4456
}


def dev_by_parsing(specialty: str, city: str) -> list:
    domain = 'https://jobs.dev.by/'
    params = {'filter[specialization_title]': f'{specialty.title()}',
              'filter[city_id][]': cities[city]}
    status, content = get_site_page(domain, params).values()
    if status != 200:
        return status
    vacancies = []
    blocks = content.find_all('div', class_='vacancies-list-item__body')
    for block in blocks:
        try:
            title = block.find('div', attrs={
                'class': ['premium-vacancy__title', 'vacancies-list-item__position']
            }).text
            description_block = block.find_all('div', attrs={
                'class': ['premium-vacancy__row', 'vacancies-list-item__technology-tag__name']
            })
            description = ', '.join([a.text for a in description_block])
            company = block.find(['a', 'div'], attrs={
                'class': ['premium-vacancy__link', 'js-vacancy__footer__company-name', 'vacancies-list-item__company']
            }).text
            url = domain + block.a['href']
            vacancies.append({
                'title': title,
                'description': description,
                'company': company,
                'url': url,
                'site': 'https://dev.by/'
            })
        except AttributeError:
            pass
    return vacancies
