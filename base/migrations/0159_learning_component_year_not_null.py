# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0158_learning_unit_component_clean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningunitcomponent',
            name='learning_component_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.LearningComponentYear'),
        ),
    ]

