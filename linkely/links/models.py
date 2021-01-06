from urllib.parse import urlparse
from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .scraper import scrape, ScraperError


class User(AuthUser):
    class Meta:
        proxy = True

    def follow(self, other):
        Follow(follower=self, followed=other).save()


class Article(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(max_length=500)
    description = models.TextField()
    tags = models.CharField(max_length=50)
    date = models.DateTimeField("date added", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s - %s" % (self.title, self.url)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def scrape(self):
        scrape(self)
        self.save()

    def title_or_fallback(self):
        if self.title:
            return self.title
        try:
            urlparts = urlparse(self.url)
            title = urlparts.netloc + urlparts.path
            return f"{title[:75]}…" if len(title) > 75 else title
        except:
            return self.url

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "user": self.user.username,
        }


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "followed")

    def clean(self):
        if self.follower == self.followed:
            raise ValidationError(_("Cannot follow oneself."))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.follower}=>{self.followed}"
