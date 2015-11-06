# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_produtoprofiles_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoprofiles',
            name='preco',
            field=models.CharField(verbose_name='preco', max_length=10, help_text='R$ 0,00'),
        ),
    ]
