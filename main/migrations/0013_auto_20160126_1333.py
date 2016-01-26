# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160126_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paragraphimage',
            name='paragraph',
        ),
        migrations.RemoveField(
            model_name='paragraphvideo',
            name='paragraph',
        ),
        migrations.AlterModelOptions(
            name='paragraph',
            options={'ordering': ['display_order']},
        ),
        migrations.AddField(
            model_name='paragraph',
            name='image',
            field=models.FileField(blank=True, upload_to='paragraphimages/%Y/%m/%d', null=True),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='layout',
            field=models.CharField(default='LR', max_length=2),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='video_link',
            field=models.CharField(help_text='Only support youtube embedded video link, e.g https://www.youtube.com/embed/mqH2LLVloE4', max_length=500, blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ParagraphImage',
        ),
        migrations.DeleteModel(
            name='ParagraphVideo',
        ),
    ]
