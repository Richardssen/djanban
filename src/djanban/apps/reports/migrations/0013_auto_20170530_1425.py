# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 12:25
from __future__ import unicode_literals

from django.db import migrations




class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0069_auto_20170530_1425'),
        ('reports', '0012_auto_20170325_1656'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='cardmovement',
            index_together={
                ('board', 'card', 'datetime'),
                ('board', 'type', 'source_list', 'destination_list'),
                (
                    'board',
                    'card',
                    'source_list',
                    'datetime',
                    'destination_list',
                ),
                ('board', 'destination_list', 'datetime'),
                (
                    'board',
                    'card',
                    'destination_list',
                    'datetime',
                    'source_list',
                ),
            },
        )
    ]
