# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-27 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='order_pay',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
