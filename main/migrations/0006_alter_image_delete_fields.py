# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_image_page_notnull'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='uploaded_at',
        ),
        migrations.RemoveField(
            model_name='image',
            name='uploaded_by',
        ),
    ]
