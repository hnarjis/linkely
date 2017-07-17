from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .wiring import es_client
from .models import Article
from .scraper import scrape

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login'
    template_name = 'links/index.html'
    context_object_name = 'latest_articles'

    def get_queryset(self):
        return Article.objects.order_by('-date')[:20]

@login_required(login_url='/login')
def add(request):
    try:
        url = request.POST['url']
    except KeyError:
        raise Exception("Missing URL.")
    else:
        article = Article(url=url, user=request.user)
        article.save()
        scrape(article)
        return HttpResponseRedirect(reverse('index'))

@login_required(login_url='/login')
def search(request):
    querystring = request.GET.get('q', '')
    context = {'search_results': None, 'error': None, 'search_query': querystring}

    # TODO: empty query should show zero results
    try:
        es = es_client()
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
        context['error'] = 'Something went wrong :( %r' % ex

    articles = [Article.objects.get(pk=article['_id'])
                for article
                in res.get('hits', []).get('hits', [])]

    context['search_results'] = articles

    return render(request, 'links/search_result.html', context)

def login(request):
    context = {}

    if request.POST.get('username'):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context['error'] = 'Wrong username or password.'

    return render(request, 'login/login.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('login'))
