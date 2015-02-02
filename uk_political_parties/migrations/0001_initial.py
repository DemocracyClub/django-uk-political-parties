# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('party_id', models.CharField(max_length=100, serialize=False, primary_key=True, blank=True)),
                ('party_name', models.CharField(max_length=765)),
                ('registered_date', models.DateField(default=datetime.datetime.today)),
                ('party_address', models.TextField(blank=True)),
                ('postcode', models.CharField(max_length=15, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('status', models.CharField(max_length=100, blank=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from=b'party_name', editable=False, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Parties',
            },
            bases=(models.Model,),
        ),
    ]
