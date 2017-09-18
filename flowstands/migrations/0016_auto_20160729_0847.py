# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0015_flowstand_placeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowstand',
            name='serial_number',
            field=models.CharField(max_length=20, verbose_name='\u0417\u0430\u0432.\u043d\u043e\u043c\u0435\u0440'),
        ),
    ]
