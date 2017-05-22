from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.URLField()
    site = models.URLField()
    id = models.IntegerField(primary_key=True)
