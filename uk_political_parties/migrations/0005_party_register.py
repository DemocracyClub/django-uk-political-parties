# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0004_auto_20150111_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='register',
            field=models.CharField(default='Great Britain', help_text=b'Country the party is registered in', max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
