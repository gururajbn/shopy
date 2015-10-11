# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151011_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='weight',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
