# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-4-24 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=45, null=True)),
                ('email', models.CharField(max_length=45, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('date_of_birth', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
