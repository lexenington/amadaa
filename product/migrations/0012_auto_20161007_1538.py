# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 15:38
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20161007_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default=''),
        ),
    ]
