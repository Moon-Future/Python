# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0003_messageuser_updatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageuser',
            name='UpdateTime',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
