from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from elasticsearch import Elasticsearch
from .models import Article
from .scraper import scrape

class IndexView(generic.ListView):
    template_name = 'links/index.html'
    context_object_name = 'latest_articles'

    def get_queryset(self):
        return Article.objects.order_by('-date')[:20]


def add(request):
    try:
        url = request.POST['url']
    except KeyError:
        raise Exception("Missing URL.")
    else:
        article = Article(url=url)
        article.save()
        scrape(article)
        return HttpResponseRedirect(reverse('links:index'))


def search(request):
    querystring = request.GET.get('q', '')
    context = {'search_results': None, 'error': None, 'search_query': querystring}

    # TODO: empty query should show zero results
    # TODO: make an elasticsearch client factory or something
    try:
        es = Elasticsearch(['http://elastic:changeme@localhost:9200'])
        query = {
            "query": {
                "multi_match" : {
                    "query": querystring,
                    "fields": ["title", "body"]
                }
            }
        }
        res = es.search(index="articles", body=query)
    except Exception as ex:
        context['error': 'Something went wrong :( %r' % ex]

    articles = [Article.objects.get(pk=article['_id'])
                for article
                in res.get('hits', []).get('hits', [])]

    context['search_results'] = articles

    return render(request, 'links/search_result.html', context)

def login(request):
    return render(request, 'login/login.html')
