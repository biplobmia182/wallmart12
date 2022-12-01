from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)

class Product2(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    
class Product3(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)