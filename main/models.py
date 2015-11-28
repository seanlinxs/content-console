import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class SiteOwner(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 50)

    def __str__(self):
        return "{0}<{1}>".format(self.name, self.email)


class Website(models.Model):
    name = models.CharField(max_length = 200)
    owner = models.ForeignKey(SiteOwner)
    
    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length = 200)
    site = models.ForeignKey(Website)
    title = models.CharField(max_length = 200)
    heading = models.TextField()

    def __str__(self):
        return "{0} - {1}".format(self.name, slef.title)


class TextBlock(models.Model):
    name = models.CharField(max_length = 200)
    page = models.ForeignKey(Page)
    content = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length = 200)
    url = models.CharField(max_length = 500)
    path = models.CharField(max_length = 500)
    size = models.BigIntegerField()
    uploaded_at = models.DateTimeField()
    uploaded_by = models.ForeignKey(SiteOwner)

    def __str__(self):
        return "{0}({1}) - {2}".format(self.name, self.size, self.url)

    def was_uploaded_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days = 1)) <= self.uploaded_at <= now
