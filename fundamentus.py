import bs4
import requests
from datetime import datetime
import pandas as pd


def get_tickers(segment=73):
    url = 'https://www.fundamentus.com.br/resultado.php?segmento=' + str(segment)
    html = get_html(url)
    tickers = []
    for table in html.select('tr'):
        ticker = table.get_text().strip()[:6].strip()
        tickers.append(ticker)
    return tickers[1:]


def get_html(url):
    agent = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=agent)
    html = bs4.BeautifulSoup(page.text, 'html.parser')
    return html


def get_data(html):
    tables = html.select('table.w728')
    data = {
        'ticker': extract_from(tables[0], 0),
        'price': format_number(extract_from(tables[0], 1)),
        'price_date': format_date(extract_from(tables[0], 3)),
        'sector': extract_from(tables[0], 6),
        'subsector': extract_from(tables[0], 8),
        'statement_date': format_date(extract_from(tables[1], 1)),
        'pl': format_number(extract_from(tables[2], 0)),
        'pvpa': format_number(extract_from(tables[2], 2)),
        'net_margin': format_number(extract_from(tables[2], 9)),
        'yield': format_number(extract_from(tables[2], 14)),
        'roe': format_number(extract_from(tables[2], 15)),  # gross debt / net worth
        'ev_ebit': format_number(extract_from(tables[2], 18)),
        'gd_nw': format_number(extract_from(tables[2], 19))
    }
    return data


def extract_from(table, position):
    return table.select('.data .txt')[position].string.strip()


def format_number(number):
    if number == '-':
        return None
    number = number.replace('.', '').replace(',', '.').replace('%', '')
    return float(number)


def format_date(date):
    return datetime.strptime(date, '%d/%m/%Y').date()


def to_dataframe(dictionary, columns):
    df = pd.DataFrame(columns=columns)
    for data in dictionary:
        df.loc[len(df)] = list(data.values())
    return df


if __name__ == "__main__":
    url = 'https://www.fundamentus.com.br/detalhes.php?papel='
    segments = {
        'banks': 73,
        'sanitation': 33,
        'electrical_energy': 32,
        'food': 15,
        'financial_services': 78
    }
    data = []

    tickers = get_tickers(segments['financial_services'])
    total = len(tickers)
    for ticker in tickers:
        print('{:.2f}%'.format(100 * (tickers.index(ticker) + 1) / total))
        html = get_html(url + ticker)
        data.append(get_data(html))
    df = to_dataframe(data, data[0].keys())
    print(df)
    df.to_csv('data.csv', sep=';')
