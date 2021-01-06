from django.conf.urls import url

from . import views

app_name = "links"
urlpatterns = [
    url(r"^add$", views.add, name="add"),
    url(r"^search$", views.search, name="search"),
    url(r"^user/(?P<username>\w+)$", views.user, name="user"),
]
