# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0002_partyemblem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ('-weight', 'party_name'), 'verbose_name_plural': 'Parties'},
        ),
        migrations.AddField(
            model_name='party',
            name='weight',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partyemblem',
            name='party',
            field=models.ForeignKey(related_name=b'emblems', to='uk_political_parties.Party'),
        ),
    ]
