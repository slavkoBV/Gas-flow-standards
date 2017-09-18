# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowstands', '0002_auto_20160614_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('agent', models.CharField(max_length=100, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430 \u043e\u0441\u043e\u0431\u0430')),
                ('address', models.CharField(max_length=256, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0430', blank=True)),
                ('contacts', models.CharField(max_length=256, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0456 \u0434\u0430\u043d\u0456', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430 \u043f\u043e\u0448\u0442\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u043b\u0430\u0441\u043d\u0438\u043a',
                'verbose_name_plural': '\u0412\u043b\u0430\u0441\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Manufactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('agent', models.CharField(max_length=100, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430 \u043e\u0441\u043e\u0431\u0430')),
                ('address', models.CharField(max_length=256, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0430', blank=True)),
                ('contacts', models.CharField(max_length=256, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0456 \u0434\u0430\u043d\u0456', blank=True)),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430 \u043f\u043e\u0448\u0442\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a',
                'verbose_name_plural': '\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u043b\u0430\u0441\u0442\u044c',
                'verbose_name_plural': '\u041e\u0431\u043b\u0430\u0441\u0442\u0456',
            },
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u043b\u0430\u0441\u043d\u0438\u043a', to='flowstands.Customer', null=True),
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='manufactor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a', to='flowstands.Manufactor', null=True),
        ),
        migrations.AlterField(
            model_name='flowstand',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c', to='flowstands.Region', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c', to='flowstands.Region', null=True),
        ),
    ]
