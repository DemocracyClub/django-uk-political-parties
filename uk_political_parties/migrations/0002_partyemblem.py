# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyEmblem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emblem_url', models.URLField(blank=True)),
                ('party', models.ForeignKey(to='uk_political_parties.Party')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
