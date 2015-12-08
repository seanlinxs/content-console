# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_add_page_to_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='textblock',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='website',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='image',
            name='page',
            field=models.ForeignKey(to='main.Page'),
        ),
    ]
