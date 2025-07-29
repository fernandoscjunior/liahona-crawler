#make requests
import requests
from random import choice

user_agents = ["Mozzilla/5.0 (Windows NT 10.0; Win64; x64)", 
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" ]

chameleon = {"User-Agent": choice(user_agents),
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
             "Referer": "https://google.com",
             "Accept-Language": "en-US,en;q=0.9"}

def download_url(url):
    confirmation = ban_filter(url) #gets only allowed urls

    if confirmation == False:
        return False
    else:
        url_final = requests.get(url, headers=chameleon, timeout=3)
        return url_final
    
def ban_filter(url): #verifies with the site allows crawling
    if url[-1] != "/":
        url = f"{url}/robots.txt"
    else:
        url = f"{url}robots.txt"

    url_bot = requests.get(url, headers=chameleon)

    #checks status to be sure we ain't gonna be banned
    if url_bot.status_code == 200:
        return True
    elif url_bot.status_code == 404:
        return True
    else:
        return False