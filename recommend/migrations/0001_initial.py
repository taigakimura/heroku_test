#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Generated by Django 2.1.1 on 2018-10-07 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('mailaddress', models.TextField()),
                ('login_pw', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('alcohol_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_name', models.TextField()),
                ('alco_name', models.CharField(max_length=20)),
                ('image', models.TextField(blank=True, null=True)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('option_data', models.TextField(blank=True, null=True)),
                ('learning_data', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recommend.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.IntegerField(primary_key=True, serialize=False)),
                ('option_contents1', models.CharField(max_length=30)),
                ('option_contents2', models.CharField(max_length=30)),
                ('option_contents3', models.CharField(blank=True, max_length=30, null=True)),
                ('option_contents4', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('ques_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ques_contents', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recommend.Question'),
        ),
    ]