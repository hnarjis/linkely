from django.conf.urls import url

from . import views

app_name = 'links'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^search$', views.search, name='search'),
]
