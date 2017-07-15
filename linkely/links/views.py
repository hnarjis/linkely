from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
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
