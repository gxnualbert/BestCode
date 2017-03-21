# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-21 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.AutoField(primary_key=True, serialize=False)),
                ('vote_desc', models.CharField(max_length=1024)),
                ('vote_start_time', models.DateTimeField()),
                ('vote_end_time', models.DateTimeField()),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='VoteItem',
            fields=[
                ('vote_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('vote_users', models.CharField(max_length=4096)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
                ('vote_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Vote')),
            ],
        ),
    ]