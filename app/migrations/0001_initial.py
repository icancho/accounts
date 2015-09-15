# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesRegistry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expenses', models.CharField(max_length=50)),
                ('income', models.CharField(max_length=50)),
                ('income_date', models.DateTimeField()),
                ('expenses_date', models.DateTimeField()),
                ('expenses_concept', models.TextField(max_length=50)),
                ('income_concept', models.TextField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
