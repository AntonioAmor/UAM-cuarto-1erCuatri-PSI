# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20171218_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Cliente'),
        ),
    ]