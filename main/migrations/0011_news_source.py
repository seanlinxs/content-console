# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_videolink'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(choices=[('INLINE', 'Inline Text'), ('REFERENCE', 'External Link')], default='INLINE', max_length=20),
        ),
    ]
