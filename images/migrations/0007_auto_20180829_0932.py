# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0006_remove_uploadedimage_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('description', models.CharField(max_length=1000, blank=True, null=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(related_name='uploaded_images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='uploadedimage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uploadedimage',
            name='users_like',
        ),
        migrations.DeleteModel(
            name='UploadedImage',
        ),
    ]
