# -*- coding: utf-8 -*-


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
                ('postcode', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('status', models.CharField(max_length=100, blank=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='party_name', editable=False, blank=True)),
                ('party_type', models.CharField(max_length=100, blank=True)),
                ('register', models.CharField(help_text='Country the party is registered in', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Parties',
            },
            bases=(models.Model,),
        ),
    ]
