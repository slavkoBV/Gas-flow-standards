# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0008_auto_20160727_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowstand',
            name='date_calibr',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u0430\u043b\u0456\u0431\u0440\u0443\u0432\u0430\u043d\u043d\u044f', blank=True),
        ),
    ]
