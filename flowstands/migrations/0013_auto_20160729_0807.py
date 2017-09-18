# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0012_auto_20160728_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['region'], 'verbose_name': '\u0412\u043b\u0430\u0441\u043d\u0438\u043a', 'verbose_name_plural': '\u0412\u043b\u0430\u0441\u043d\u0438\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='flowstand',
            options={'ordering': ['region'], 'verbose_name': '\u0420\u043e\u0431\u043e\u0447\u0438\u0439 \u0435\u0442\u0430\u043b\u043e\u043d', 'verbose_name_plural': '\u0420\u043e\u0431\u043e\u0447\u0456 \u0435\u0442\u0430\u043b\u043e\u043d\u0438'},
        ),
        migrations.AlterField(
            model_name='manufactor',
            name='agent',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430 \u043e\u0441\u043e\u0431\u0430', blank=True),
        ),
    ]
