import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Website(models.Model):
    name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User)
    
    
    class Meta:
        ordering = ['id']

    
    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=200)
    site = models.ForeignKey(Website)
    title = models.CharField(max_length=200)
    heading = models.TextField(blank=True)

    
    class Meta:
        ordering = ['id']

    
    def __str__(self):
        return self.name


class TextBlock(models.Model):
    name = models.CharField(max_length=200)
    page = models.ForeignKey(Page)
    content = models.TextField()


    class Meta:
        ordering = ['id']

    
    def __str__(self):
        return self.name


class Paragraph(models.Model):
    name = models.CharField(max_length=200)
    page = models.ForeignKey(Page)
    markdown = models.TextField()
    display_order = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class ParagraphImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='paragraphimages/%Y/%m/%d')
    paragraph = models.ForeignKey(Paragraph)
    LAYOUTS = (
        ('ABOVE', 'On top of the paragraph'),
        ('LEFT', 'Left aside of the paragraph'),
        ('RIGHT', 'Right aside of the paragraph'),
        ('BELOW', 'Under the paragraph')
    )
    layout = models.CharField(max_length=10, choices=LAYOUTS, default='RIGHT')

    
    class Meta:
        ordering = ['id']

    
    def __str__(self):
        return self.name


class ParagraphVideo(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500, help_text="Only support youtube embedded video link, e.g https://www.youtube.com/embed/mqH2LLVloE4")
    paragraph = models.ForeignKey(Paragraph)
    LAYOUTS = (
        ('ABOVE', 'On top of the paragraph'),
        ('LEFT', 'Left aside of the paragraph'),
        ('RIGHT', 'Right aside of the paragraph'),
        ('BELOW', 'Under the paragraph')
    )
    layout = models.CharField(max_length=10, choices=LAYOUTS, default='ABOVE')


    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.name


class PageImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='pageimages/%Y/%m/%d')
    page = models.ForeignKey(Page)

    
    class Meta:
        ordering = ['id']

    
    def __str__(self):
        return self.name


class VideoLink(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500, help_text="Only support youtube embedded video link, e.g https://www.youtube.com/embed/mqH2LLVloE4")
    page = models.ForeignKey(Page)


    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='newsimages/%Y/%m/%d')
    site = models.ForeignKey(Website)
    NEWS_SOURCES = (
        ('INLINE', 'Inline Text'),
        ('REFERENCE', 'External Link')
    )
    source = models.CharField(max_length=20, choices=NEWS_SOURCES, default='INLINE')


    class Meta:
        ordering = ['id']


    def __str__(self):
        return self.title
