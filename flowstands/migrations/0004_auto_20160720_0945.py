# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0003_auto_20160720_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowstand',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='flowstand',
            name='manufactor',
        ),
    ]
