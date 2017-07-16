from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(max_length=500)
    description = models.TextField()
    tags = models.CharField(max_length=50)
    date = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.title, self.url)
