# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('castar', '0003_auto_20170516_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('HS', 'Head Shot'), ('WP', 'Western Party Wear'), ('IP', 'Indian Party Wear'), ('SW', 'Swim Wear'), ('CW', 'Casual Wear')], default='CW', max_length=2)),
                ('photos', models.FileField(max_length=200, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
