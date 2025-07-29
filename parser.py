#gets clean url and gets html, and hyperlinks.

from bs4 import BeautifulSoup
from urllib.parse import urljoin

def html_parser(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    for tag in soup.select('script, style, header, footer, nav, aside, .sidebar, .ads, .menu'):
        tag.decompose()
    return soup

def links_getter(soup):
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return links
