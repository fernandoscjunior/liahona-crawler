#crawls, and filters which links to visit and which ones were already visited
from filter import download_url
from parser import html_parser,links_getter

visited_urls = []
urls_to_visit = ["https://churchofjesuschrist.org"]

def add_url_to_visit(url):
    if url not in visited_urls and url not in urls_to_visit:
        urls_to_visit.append(url)

def crawl(url):
    url_pure = download_url(url)
    if url_pure == False:
        print("This site doesn't like requests...")

    soup = html_parser(url_pure)
    for url in links_getter(soup):
        add_url_to_visit(url)

def run():
    crawls_num = 0
    while urls_to_visit and crawls_num < 20:
        url = urls_to_visit.pop(0)
        if url.startswith("h"):
            try:
                crawl(url)
                print(f"crawled succesfully: {url}")
            except Exception:
                print(f"Failed to crawl {url}")
            finally:
                visited_urls.append(url)
                crawls_num += 1
        else:
            pass