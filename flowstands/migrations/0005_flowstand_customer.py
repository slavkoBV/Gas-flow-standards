# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0004_auto_20160720_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowstand',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u043b\u0430\u0441\u043d\u0438\u043a', to='flowstands.Customer', null=True),
        ),
    ]
