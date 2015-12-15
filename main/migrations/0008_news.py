# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_image_rename'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('content', models.TextField()),
                ('image', models.FileField(upload_to='newsimages/%Y/%m/%d')),
                ('site', models.ForeignKey(to='main.Website')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
