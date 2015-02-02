# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0005_party_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='register',
            field=models.CharField(help_text=b'Country the party is registered in', max_length=255, null=True, blank=True),
        ),
    ]
