# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151002_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtoprofiles',
            name='preco',
            field=models.CharField(verbose_name='preco', default=0, max_length=10),
            preserve_default=False,
        ),
    ]
