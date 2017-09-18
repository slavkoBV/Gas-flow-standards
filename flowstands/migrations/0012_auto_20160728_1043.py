# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0011_auto_20160728_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c', to='flowstands.Region', null=True),
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0412\u043b\u0430\u0441\u043d\u0438\u043a', to='flowstands.Customer', null=True),
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c', to='flowstands.Region', null=True),
        ),
    ]
