# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151201_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='heading',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200, help_text="Title will be displayed in both browser's title bar and page title."),
        ),
        migrations.AlterField(
            model_name='textblock',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
