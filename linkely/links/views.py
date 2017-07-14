#from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-date')[:20]
    output = ', '.join([a.title for a in latest_articles])
    return HttpResponse(output)
