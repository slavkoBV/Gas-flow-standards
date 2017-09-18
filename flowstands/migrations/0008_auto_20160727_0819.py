# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0007_auto_20160721_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowstand',
            name='date_calibr',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0456\u0431\u0440\u0443\u0432\u0430\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='flow_range',
            field=models.CharField(max_length=30, verbose_name='\u0414\u0456\u0430\u043f\u0430\u0437\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='serial_number',
            field=models.CharField(max_length=20, verbose_name='\u0417\u0430\u0432\u043e\u0434\u0441\u044c\u043a\u0438\u0439 \u043d\u043e\u043c\u0435\u0440'),
        ),
    ]
