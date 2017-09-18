# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0019_auto_20160830_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalStandard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0435\u0442\u0430\u043b\u043e\u043d\u0430', blank=True)),
                ('short_name', models.CharField(max_length=30, verbose_name='\u041f\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044f')),
                ('flow_range', models.CharField(max_length=30, verbose_name='\u0414\u0456\u0430\u043f\u0430\u0437\u043e\u043d \u0432\u0438\u0442\u0440\u0430\u0442')),
                ('image', models.FileField(upload_to=b'images/', verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('description', models.TextField(max_length=1000, verbose_name='\u041e\u043f\u0438\u0441 \u0435\u0442\u0430\u043b\u043e\u043d\u0430', blank=True)),
                ('keeper', models.CharField(max_length=40, verbose_name='\u0412\u0447\u0435\u043d\u0438\u0439 \u0437\u0431\u0435\u0440\u0456\u0433\u0430\u0447', blank=True)),
                ('artefacts', models.CharField(max_length=256, verbose_name='\u0422\u0438\u043f\u0438 \u0434\u043e\u0441\u043b\u0456\u0434\u0436\u0443\u0432\u0430\u043d\u0438\u0445 \u043f\u0440\u0438\u043b\u0430\u0434\u0456\u0432', blank=True)),
                ('diameters', models.CharField(max_length=200, verbose_name='\u0414\u0456\u0430\u043c\u0435\u0442\u0440\u0438 \u0443\u043c\u043e\u0432\u043d\u0438\u0445 \u043f\u0440\u043e\u0445\u043e\u0434\u0456\u0432', blank=True)),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u0438\u0439 \u0435\u0442\u0430\u043b\u043e\u043d',
                'verbose_name_plural': '\u041d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u0456 \u0435\u0442\u0430\u043b\u043e\u043d\u0438',
            },
        ),
    ]
