# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flowstand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=256, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c')),
                ('customer', models.CharField(max_length=256, verbose_name='\u0412\u043b\u0430\u0441\u043d\u0438\u043a')),
                ('name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('flow_range', models.CharField(max_length=256, verbose_name='\u0414\u0456\u0430\u043f\u0430\u0437\u043e\u043d')),
                ('serial_number', models.CharField(max_length=256, verbose_name='\u0417\u0430\u0432\u043e\u0434\u0441\u044c\u043a\u0438\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('manufactor', models.CharField(max_length=256, verbose_name='\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a')),
                ('certificate', models.CharField(max_length=256, null=True, verbose_name='\u0421\u0435\u0440\u0442\u0438\u0444\u0456\u043a\u0430\u0442', blank=True)),
                ('calibr_method', models.CharField(max_length=256, null=True, verbose_name='\u041c\u0435\u0442\u043e\u0434 \u043a\u0430\u043b\u0456\u0431\u0440\u0443\u0432\u0430\u043d\u043d\u044f', blank=True)),
            ],
        ),
    ]
