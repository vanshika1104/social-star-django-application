# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadedimage',
            options={'ordering': ('-created',)},
        ),
    ]
