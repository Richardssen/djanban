# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 16:11
from __future__ import unicode_literals

from django.db import migrations




class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0028_auto_20160925_1809'),
        ('members', '0008_auto_20160923_2056'),
        ('dev_environment', '0002_auto_20160921_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interruption',
            options={
                'verbose_name': 'Interruption',
                'verbose_name_plural': 'Interruptions',
            },
        ),
        migrations.AlterIndexTogether(
            name='interruption',
            index_together={
                ('datetime', 'board', 'member'),
                ('member', 'datetime', 'board'),
            },
        ),
    ]
