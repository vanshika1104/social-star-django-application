# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20180830_0722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimages',
            name='user',
        ),
        migrations.DeleteModel(
            name='UploadedImages',
        ),
    ]
