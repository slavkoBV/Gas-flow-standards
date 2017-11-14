# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0020_nationalstandard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name='\u043d\u0430\u0437\u0432\u0430')),
                ('edition', models.IntegerField(verbose_name='\u0440\u0435\u0434\u0430\u043a\u0446\u0456\u044f')),
                ('file', models.FileField(upload_to=b'/documents', verbose_name='\u0444\u0430\u0439\u043b')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u0438\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u041d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u0456 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0438',
            },
        ),
    ]
