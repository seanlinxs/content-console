# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('path', models.CharField(max_length=500)),
                ('size', models.BigIntegerField()),
                ('uploaded_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('heading', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SiteOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('page', models.ForeignKey(to='main.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(to='main.SiteOwner')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(to='main.Website'),
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded_by',
            field=models.ForeignKey(to='main.SiteOwner'),
        ),
    ]
