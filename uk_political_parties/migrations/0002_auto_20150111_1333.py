# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='postcode',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
