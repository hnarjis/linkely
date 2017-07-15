from bs4 import BeautifulSoup
import requests
import re

def normalize_url(url):
    if not url.lower().startswith('http'):
        return 'http://%s' % url
    return url

def guess_title(document, url):
    try:
        return document.find("title").text
    except:
        pass

    document_name = url.split('/')[-1]
    document_name = re.sub('[-_]', ' ', document_name)
    return document_name.capitalize()

def scrape(article):
    article.url = normalize_url(article.url)
    response = requests.get(article.url)
    document = None
    if response.ok:
        document = BeautifulSoup(response.text, 'lxml')
    title = guess_title(document, article.url)
    if title:
        article.title = title
    article.save()
