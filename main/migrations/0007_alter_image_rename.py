# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_image_delete_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('image', models.FileField(upload_to='pageimages/%Y/%m/%d')),
                ('page', models.ForeignKey(to='main.Page')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='page',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
