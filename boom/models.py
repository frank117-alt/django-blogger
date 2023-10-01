from django.db import models

# Create your models here.
import datetime

class bloger(models.Model):
    
    title= models.CharField(max_length=60)
    text = models.TextField()
    pub_date= models.DateTimeField('fecha')
    upload = models.FileField(upload_to='bloger/img')


class product(models.Model):

       name = models.CharField(max_length=100)
       description = models.TextField()
       precio = models.IntegerField()
       total = models.IntegerField()
       upload = models.FileField(upload_to='bloger/product')
