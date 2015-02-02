# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0003_party_minor_party'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='minor_party',
        ),
        migrations.AddField(
            model_name='party',
            name='party_type',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
