# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flowstand',
            options={'verbose_name': '\u0420\u043e\u0431\u043e\u0447\u0438\u0439 \u0435\u0442\u0430\u043b\u043e\u043d', 'verbose_name_plural': '\u0420\u043e\u0431\u043e\u0447\u0456 \u0435\u0442\u0430\u043b\u043e\u043d\u0438'},
        ),
        migrations.RenameField(
            model_name='flowstand',
            old_name='calibr_method',
            new_name='calibr_type',
        ),
    ]
