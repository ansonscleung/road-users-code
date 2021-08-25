from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

pages = set()
base = "https://www.td.gov.hk/tc/road_safety/road_users_code"

def fetch_link(url: str):
    req = requests.get(url)
    encoding = req.encoding if 'charset' in req.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(req.content, from_encoding=encoding)
    print(soup.find('body'))
    for link in soup.find_all('a', href=True):
        path = urljoin(url, link['href'])
        if path.startswith(base) and path not in pages:
            pages.add(path)
            fetch_link(path)

fetch_link(base)
with open('pages.txt', 'w') as f:
    for page in pages:
        print(page, file=f)
