# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-03 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0140_auto_20170627_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationaddress',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
