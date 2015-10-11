# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151011_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='ethnicity',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
