from bs4 import BeautifulSoup
import requests
import re
from .wiring import es_client

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
    # TODO: fix when not a valid url
    article.url = normalize_url(article.url)
    response = requests.get(article.url)
    document = None
    if response.ok:
        document = BeautifulSoup(response.content, 'lxml')
    title = guess_title(document, article.url)
    if title:
        article.title = title
    article.save()
    index(article, document)

def index(article, document):
    es = es_client()

    doc = {
        'title': article.title,
        'url': article.url,
        'body': document.get_text()
    }

    res = es.index(index="articles", doc_type='article', id=article.id, body=doc)
    print(res['created'])

    # NOTE: remove this for high volume sites
    es.indices.refresh(index="articles")
