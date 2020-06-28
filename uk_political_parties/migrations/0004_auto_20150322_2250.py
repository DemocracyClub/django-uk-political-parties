# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uk_political_parties', '0003_auto_20150204_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partyemblem',
            options={'ordering': ('emblem_url',)},
        ),
    ]
