# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20180830_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
