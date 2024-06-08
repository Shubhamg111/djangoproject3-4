from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name