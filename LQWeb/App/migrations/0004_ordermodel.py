# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-27 03:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20190722_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(default=datetime.datetime.now)),
                ('order_num', models.CharField(max_length=20)),
                ('get_user', models.CharField(max_length=100)),
                ('send_address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'lq_order',
            },
        ),
    ]
