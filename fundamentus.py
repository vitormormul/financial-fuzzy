import bs4
import requests


def extract_data(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=agent)
    html = bs4.BeautifulSoup(page.text, 'html.parser')
    return html


def extract_from(table, position):
    return table.select('.data .txt')[position].string.strip()


def format_number(number):
    return number.replace('.', '').replace(',', '.').replace('%', '')


def get_data(html):
    tables = html.select('table.w728')
    data = {
        'ticker': extract_from(tables[0], 0)
    }
    return data


if "__main__" == __name__:
    url = 'https://www.fundamentus.com.br/detalhes.php?papel=B3SA3'
    html = extract_data(url)
    data = get_data(html)
    print(data)

