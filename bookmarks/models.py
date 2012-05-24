from django.db import models
# Create your models here.

class Link(models.Model):
    url = models.URLField(unique=True)

from django.contrib.auth.models import User

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)
