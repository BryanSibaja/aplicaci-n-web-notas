# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-24 02:22
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20171114_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='cuerpo',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
