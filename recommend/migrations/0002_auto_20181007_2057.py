#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Generated by Django 2.1.1 on 2018-10-07 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='alcohol',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'managed': False},
        ),
    ]