# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0002_auto_20150111_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='minor_party',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
