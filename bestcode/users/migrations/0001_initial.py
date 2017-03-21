# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-21 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryDepartment',
            fields=[
                ('primary_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('programming_language_id', models.AutoField(primary_key=True, serialize=False)),
                ('language_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryDepartment',
            fields=[
                ('secondary_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
                ('photo', models.CharField(max_length=256)),
                ('programming_languages', models.CharField(max_length=256)),
                ('primary_department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.PrimaryDepartment')),
                ('secondary_department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.SecondaryDepartment')),
            ],
        ),
    ]
