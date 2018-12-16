# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_uploadedimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadedimage',
            old_name='image',
            new_name='pic',
        ),
    ]
