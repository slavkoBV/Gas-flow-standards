# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0014_auto_20160729_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowstand',
            name='placeholder',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0430 \u0440\u043e\u0437\u043c\u0456\u0449\u0435\u043d\u043d\u044f', blank=True),
        ),
    ]
