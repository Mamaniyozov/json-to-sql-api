from django.db import models

# Create your models here.
class Smartphone(models.Model):
    price = models.FloatField()

    img_url = models.CharField(max_length=255,default='image')
    color = models.CharField(max_length=20)
    ram = models.IntegerField()
    
    memory = models.IntegerField(blank=True)
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    # Create a timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.id} {self.name}"