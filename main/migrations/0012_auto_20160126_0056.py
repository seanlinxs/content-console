# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_news_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('markdown', models.TextField()),
                ('display_order', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ParagraphImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='paragraphimages/%Y/%m/%d')),
                ('layout', models.CharField(choices=[('ABOVE', 'On top of the paragraph'), ('LEFT', 'Left aside of the paragraph'), ('RIGHT', 'Right aside of the paragraph'), ('BELOW', 'Under the paragraph')], default='RIGHT', max_length=10)),
                ('paragraph', models.ForeignKey(to='main.Paragraph')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ParagraphVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(help_text='Only support youtube embedded video link, e.g https://www.youtube.com/embed/mqH2LLVloE4', max_length=500)),
                ('layout', models.CharField(choices=[('ABOVE', 'On top of the paragraph'), ('LEFT', 'Left aside of the paragraph'), ('RIGHT', 'Right aside of the paragraph'), ('BELOW', 'Under the paragraph')], default='ABOVE', max_length=10)),
                ('paragraph', models.ForeignKey(to='main.Paragraph')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='videolink',
            name='link',
            field=models.CharField(help_text='Only support youtube embedded video link, e.g https://www.youtube.com/embed/mqH2LLVloE4', max_length=500),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='page',
            field=models.ForeignKey(to='main.Page'),
        ),
    ]
