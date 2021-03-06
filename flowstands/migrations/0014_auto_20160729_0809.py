# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0013_auto_20160729_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowstand',
            name='manufactor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a', blank=True, to='flowstands.Manufactor', null=True),
        ),
    ]
