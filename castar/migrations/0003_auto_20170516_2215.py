# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castar', '0002_auto_20170516_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='starprofile',
            name='address_6',
            field=models.CharField(blank=True, help_text='Please enter your pin code.', max_length=6, verbose_name='Pin Code'),
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='address_1',
            field=models.CharField(blank=True, help_text='Please enter your buildin name and flat number.', max_length=200, verbose_name='Building\\Flat Number'),
        ),
    ]
