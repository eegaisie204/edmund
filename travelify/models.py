from django.db import models

# Create your models here.

class Testimony(models.Model):
    
    desc = models.TextField()
    name = models.CharField(max_length=100)
    custometype = models.CharField(max_length=100)
    
class Place(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
class Ifem(models.Model):
    
    day = models.IntegerField()
    month = models.CharField(max_length=100)
    title = models.TextField()
    subtitle = models.TextField()
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')