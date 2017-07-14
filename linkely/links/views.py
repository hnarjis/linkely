from django.shortcuts import render
from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-date')[:20]
    return render(request, 'links/index.html', {'latest_articles': latest_articles})
