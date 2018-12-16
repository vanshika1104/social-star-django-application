# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20180829_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='slug',
        ),
    ]
