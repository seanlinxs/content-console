# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_add_unique_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='page',
            field=models.ForeignKey(to='main.Page', null=True),
        ),
    ]
