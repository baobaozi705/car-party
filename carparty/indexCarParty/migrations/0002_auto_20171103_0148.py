# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexCarParty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
