# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0010_auto_20160728_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowstand',
            name='certificate',
            field=models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0421\u0435\u0440\u0442\u0438\u0444\u0456\u043a\u0430\u0442', blank=True),
        ),
    ]
