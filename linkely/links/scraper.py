import re
from bs4 import BeautifulSoup
import requests
from .wiring import es_client


class ScraperError(Exception):
    pass


def guess_title(document, url):
    try:
        return document.find("title").text
    except:  # pylint: disable=bare-except
        pass

    document_name = url.split("/")[-1]
    document_name = re.sub("[-_]", " ", document_name)
    return document_name.capitalize()[:150]


def scrape(article):
    # TODO: This should be done in the background.
    try:
        response = requests.get(article.url, timeout=15)
        document = None
        if response.ok:
            document = BeautifulSoup(response.content, "lxml")
        title = guess_title(document, article.url)
        if title:
            article.title = title
        index(article, document)
    except Exception as err:
        raise ScraperError(str(err)) from err


def index(article, document):
    es = es_client()

    doc = {"title": article.title, "url": article.url, "body": document.get_text()}

    es.index(index="articles", doc_type="article", id=article.id, body=doc)

    # NOTE: remove this for high volume sites
    es.indices.refresh(index="articles")
