from django.db import models

# Create your models here.


class Article (models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)
    article = models.FileField(upload_to='static/media')

    class Meta:
        db_table = 'sqlite3.db'
