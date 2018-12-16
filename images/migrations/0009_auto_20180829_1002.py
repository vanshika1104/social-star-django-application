# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0008_auto_20180829_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('image', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='upload_photo',
        ),
    ]
