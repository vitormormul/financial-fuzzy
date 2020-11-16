import bs4
import requests


def get_data(url):
    agent = {"User-Agent":"Mozilla/5.0"}
    page = requests.get(url, headers=agent)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    return soup

