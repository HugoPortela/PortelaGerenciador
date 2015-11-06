# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151003_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoprofiles',
            name='categoria',
            field=models.CharField(choices=[('RF', 'Roupas Femininas'), ('RM', 'Roupas Masculinas'), ('MI', 'Moda Intima'), ('IN', 'Moda Infantil')], max_length=2),
        ),
    ]
