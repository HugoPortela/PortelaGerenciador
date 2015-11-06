# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroProdutos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=50, verbose_name='nome')),
                ('referencia', models.CharField(max_length=50, verbose_name='Referencia')),
                ('quantidade', models.CharField(max_length=5, verbose_name='quantidade')),
            ],
        ),
    ]
