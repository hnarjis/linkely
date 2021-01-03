import re
from bs4 import BeautifulSoup
import requests
from .wiring import es_client


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"


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
        headers = {"user-agent": USER_AGENT}
        response = requests.get(
            article.url, timeout=15, allow_redirects=True, headers=headers
        )
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
