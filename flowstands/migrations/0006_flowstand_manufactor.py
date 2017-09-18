# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0005_flowstand_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowstand',
            name='manufactor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a', to='flowstands.Manufactor', null=True),
        ),
    ]
