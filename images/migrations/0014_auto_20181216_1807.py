# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0013_auto_20181216_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=600),
        ),
    ]
