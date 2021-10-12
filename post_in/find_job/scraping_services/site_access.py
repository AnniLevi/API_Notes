import requests
from bs4 import BeautifulSoup as bs
import time
import random

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]


def get_site_page(domain: str, params: dict) -> dict:
    session = requests.Session()
    time.sleep(2)
    headers_nmb = random.randint(0, 2)
    request = session.get(domain, headers=headers[headers_nmb], params=params)
    # print(request.url)
    return {
        'status': request.status_code,
        'content': bs(request.content, "html.parser")
    }
