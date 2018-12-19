# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-16 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=40)),
                ('caption', models.TextField()),
                ('likes', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
