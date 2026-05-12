from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    category = models.CharField(max_length=100)

    image = models.URLField()

    def __str__(self):
        return self.name