# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default=None, upload_to='media/')),
            ],
        ),
    ]