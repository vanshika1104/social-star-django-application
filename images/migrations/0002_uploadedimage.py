# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(related_name='images_uploaded', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(blank=True, related_name='uploaded_images_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
