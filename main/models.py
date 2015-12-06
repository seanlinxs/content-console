import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Website(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    
    
    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=200)
    site = models.ForeignKey(Website)
    title = models.CharField(max_length=200, help_text="Title will be displayed in both browser's title bar and page title.")
    heading = models.TextField(blank=True)

    
    def __str__(self):
        return self.name


class TextBlock(models.Model):
    name = models.CharField(max_length=200)
    page = models.ForeignKey(Page)
    content = models.TextField()

    
    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    path = models.CharField(max_length=500)
    size = models.BigIntegerField()
    uploaded_at = models.DateTimeField()
    uploaded_by = models.ForeignKey(User)

    
    def __str__(self):
        return "{0}({1}) - {2}".format(self.name, self.size, self.url)

    
    def was_uploaded_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.uploaded_at <= now
