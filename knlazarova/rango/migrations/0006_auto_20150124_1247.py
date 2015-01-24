# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20150123_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horn_length', models.IntegerField()),
            ],
            options={
                'ordering': ['horn_length'],
                'verbose_name_plural': 'oxen',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
