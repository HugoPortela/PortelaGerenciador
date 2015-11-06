# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151002_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtoprofiles',
            old_name='nome_produto',
            new_name='nome',
        ),
    ]
