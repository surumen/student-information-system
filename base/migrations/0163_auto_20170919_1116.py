# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0162_educationgroup_permissions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entitycomponentyear',
            unique_together=set([('entity_container_year', 'learning_component_year')]),
        ),
    ]
