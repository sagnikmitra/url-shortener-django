from django.db import models

# Create your models here.
# Django Models are same things as a database. there will be basically two tables, link, uuid


class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
