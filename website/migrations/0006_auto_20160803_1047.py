# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160803_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='curso',
            field=models.CharField(default='Eng Computacao', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participante',
            name='email',
            field=models.EmailField(default='aluno@email.com', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participante',
            name='matricula',
            field=models.CharField(default='201601234567', max_length=12),
            preserve_default=False,
        ),
    ]
