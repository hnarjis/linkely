from django.shortcuts import render
from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-date')[:20]
    return render(request, 'links/index.html', {'latest_articles': latest_articles})

def add(request):
    try:
        url = request.POST['url']
    except (KeyError):
        raise Exception("Missing URL.")
    else:
        pass
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
