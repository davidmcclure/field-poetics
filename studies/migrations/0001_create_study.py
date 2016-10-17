# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'studies',
            },
        ),
    ]