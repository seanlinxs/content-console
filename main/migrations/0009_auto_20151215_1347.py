# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='textblock',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
