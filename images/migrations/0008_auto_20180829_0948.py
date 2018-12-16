# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20180829_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimages',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='upload_photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='UploadedImages',
        ),
    ]
