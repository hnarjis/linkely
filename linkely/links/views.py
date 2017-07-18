import hashlib
import json
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.admin import User
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.http import Http404
from .wiring import es_client
from .models import Article
from .scraper import scrape


class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/login'
    template_name = 'links/index.html'
    context_object_name = 'latest_articles'
    paginate_by = 25

    def get_queryset(self):
        return Article.objects.order_by('-date')


@login_required(login_url='/login')
def user(request, username):
    template_name = 'links/user.html'
    context_object_name = 'user_articles'
    articles = Article.objects.filter(user__username=username)
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        raise Http404('No user %s found' % username)

    gravatar = '//www.gravatar.com/avatar/{hash}?s=80'.format(
        hash=hashlib.md5(user.email.encode('latin-1').strip().lower()).hexdigest())
    return render(request, 'links/user.html', {'user_articles': articles, 'profile': user, 'gravatar': gravatar})


@login_required(login_url='/login')
def add(request):
    error = None
    try:
        data = json.loads(request.body)
        article = Article(url=data['url'], user=request.user)
        article.save() # We need an id for the article before it's scraped
        scrape(article)
        article.save()
        template = loader.get_template('links/article_list_item.html')
        html = template.render({"article": article}, request)
        return JsonResponse({
            'status': 'ok',
            'article': article.as_dict(),
            'html': html
        })
    except json.JSONDecodeError:
        error = "Not valid JSON %r" % request.body
    except KeyError:
        error = "Missing url"
    except ConnectionError:
        error = "Could not connect to %r" % url
    except Exception as ex:
        error = str(ex)
    return JsonResponse({'status': 'error', 'error': error}, status=500)


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
    else:
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
