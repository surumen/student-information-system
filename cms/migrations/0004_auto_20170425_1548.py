# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 13:48
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20170317_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textlabel',
            name='entity',
            field=models.CharField(choices=[('learning_unit_year', 'learning_unit_year'), ('offer_year', 'offer_year')], max_length=25),
        ),
        migrations.AlterField(
            model_name='textlabel',
            name='order',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='translatedtext',
            name='entity',
            field=models.CharField(choices=[('learning_unit_year', 'learning_unit_year'), ('offer_year', 'offer_year')], db_index=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='translatedtext',
            name='text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
