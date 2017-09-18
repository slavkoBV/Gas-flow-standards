# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0006_flowstand_manufactor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowstand',
            name='calibr_type',
        ),
        migrations.AddField(
            model_name='flowstand',
            name='traceability',
            field=models.CharField(max_length=256, null=True, verbose_name='\u041f\u0440\u043e\u0441\u0442\u0435\u0436\u0443\u0432\u0430\u043d\u0456\u0441\u0442\u044c', blank=True),
        ),
    ]
