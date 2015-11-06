# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cadastroprodutos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoProfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(verbose_name='nome', max_length=50)),
                ('referencia', models.CharField(verbose_name='Referencia', max_length=50)),
                ('quantidade', models.CharField(verbose_name='quantidade', max_length=5)),
                ('categoria', models.CharField(choices=[('RF', 'Roupas Femininas'), ('RM', 'Roupas Masculinas')], max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='CadastroProdutos',
        ),
    ]
