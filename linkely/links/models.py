from django.db import models
from django.contrib.auth.models import User
from .scraper import scrape, ScraperError


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

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "user": self.user.username,
        }
