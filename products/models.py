from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.FileField(upload_to='static/uploads',null=True)
    trending = models.BooleanField(default=False,null=True)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

