from rest_framework import routers

from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from links.views import IndexView, login, logout, ArticleViewSet, RegisterView


router = routers.DefaultRouter()
router.register(r"articles", ArticleViewSet)

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="index"),
    url(r"^links/", include("links.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^login/$", login, name="login"),
    url(r"^logout/$", logout, name="logout"),
    # API
    path("v1/", include(router.urls)),
    path("v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/registrations/", RegisterView.as_view(), name="registrations"),
]
