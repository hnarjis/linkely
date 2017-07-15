from bs4 import BeautifulSoup
import requests

def scrape(article):
    response = requests.get(article.url)
    if not response.ok:
        return
    document = BeautifulSoup(response.text)
    try:
        title = document.find("title").text
    except:
        pass
    else:
        article.title = title
        article.save()
