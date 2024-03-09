from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155)


class Product(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.URLField()
    category = models.ManyToManyField(Category)
