from django.db import models

# Create your models here.


class about (models.Model):
    about_title = models.CharField(max_length=50)
    about_article = models.CharField(max_length=1000)
    phone_nummbers = models.IntegerField()
    address = models.CharField(max_length=100)
