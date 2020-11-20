import requests
from bs4 import BeautifulSoup as bs


def crawl():
    url = 'https://news.yahoo.co.jp/'
    resp = requests.get(url)

    return resp


def scrape(html):
    soup = bs(html, 'html.parser')
    items = soup.select('.topicsListItem')

    return items


def print_items(items):
    for item in items:
        print(item.get_text(strip=True))


if __name__ == "__main__":
    resp = crawl()
    items = scrape(resp.text)
    print_items(items)
