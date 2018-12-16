# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0009_auto_20180829_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadedimages',
            options={'ordering': ['-uploaded_at']},
        ),
        migrations.RemoveField(
            model_name='uploadedimages',
            name='image',
        ),
        migrations.RemoveField(
            model_name='uploadedimages',
            name='photo',
        ),
        migrations.AddField(
            model_name='uploadedimages',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='uploadedimages',
            name='picture',
            field=models.ImageField(null=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='uploadedimages',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='uploadedimages',
            name='uploaded_at',
            field=models.DateField(null=True, db_index=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='uploadedimages',
            name='user',
            field=models.ForeignKey(null=True, related_name='uploaded_images', to=settings.AUTH_USER_MODEL),
        ),
    ]
