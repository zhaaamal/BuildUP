from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    text = models.TextField()
    img = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    dedline = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    text = models.TextField(null=True)
    img = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


