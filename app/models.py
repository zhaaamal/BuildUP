from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    text = models.TextField()
    img = models.URLField()
