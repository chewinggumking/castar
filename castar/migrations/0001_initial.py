# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 16:39
from __future__ import unicode_literals

import castar.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StarProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth: ')),
                ('address_2', models.CharField(blank=True, help_text='Please enter your street name and\\or locality', max_length=200, verbose_name='Street\\Locality: ')),
                ('address_3', models.CharField(blank=True, help_text='Please enter the area you live in.', max_length=200, verbose_name='Area Name: ')),
                ('address_4', models.CharField(blank=True, help_text='Please enter the city you live in.', max_length=200, verbose_name='City: ')),
                ('address_5', models.CharField(blank=True, help_text='Please enter the state you live in.', max_length=200, verbose_name='State: ')),
                ('address_1', models.CharField(blank=True, help_text='Please enter your pin code.', max_length=6, verbose_name='Pin Code: ')),
                ('mobile_number', models.CharField(blank=True, help_text='Please enter your mobile number without the country code', max_length=10, validators=[castar.validators.mobile_val], verbose_name='Mobile Number +91: ')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='F', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]