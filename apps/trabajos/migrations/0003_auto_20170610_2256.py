# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajos', '0002_auto_20170610_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='cdRDC',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='dvdRDC',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='penRDC',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='trabajo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='trabajo',
            name='tipo',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='trabajos.tiposTrabajos'),
            preserve_default=False,
        ),
    ]
