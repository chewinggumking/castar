# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 16:44
from __future__ import unicode_literals

import castar.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starprofile',
            name='address_1',
            field=models.CharField(blank=True, help_text='Please enter your pin code.', max_length=6, verbose_name='Pin Code'),
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='address_2',
            field=models.CharField(blank=True, help_text='Please enter your street name and\\or locality', max_length=200, verbose_name='Street\\Locality'),
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='address_3',
            field=models.CharField(blank=True, help_text='Please enter the area you live in.', max_length=200, verbose_name='Area Name'),
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='address_4',
            field=models.CharField(blank=True, help_text='Please enter the city you live in.', max_length=200, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='address_5',
            field=models.CharField(blank=True, help_text='Please enter the state you live in.', max_length=200, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='starprofile',
            name='mobile_number',
            field=models.CharField(blank=True, help_text='Please enter your mobile number without the country code.', max_length=10, validators=[castar.validators.mobile_val], verbose_name='Mobile Number +91'),
        ),
    ]