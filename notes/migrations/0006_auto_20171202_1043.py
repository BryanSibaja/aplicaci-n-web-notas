# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-02 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20171202_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='borrado',
            field=models.BooleanField(default=False),
        ),
    ]
