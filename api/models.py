from django.db import models

# Create your models here.
class Smartphone(models.Model):
    price = models.CharField(max_length=20)
    img_url = models.CharField(max_length=255,default='image')
    color = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
