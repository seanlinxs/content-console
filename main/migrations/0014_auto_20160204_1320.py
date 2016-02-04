# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20160126_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2016, 2, 4, 13, 20, 19, 899613, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='layout',
            field=models.CharField(default='LR', choices=[('TB', 'Top text, bottom media'), ('BT', 'Bottom text, top media'), ('LR', 'Left text, right media'), ('RL', 'Right text, left media')], max_length=2),
        ),
    ]
