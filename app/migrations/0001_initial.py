# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pnum', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('caption', models.TextField(null=True)),
                ('ethnicity', models.CharField(max_length=20, null=True, choices=[(0, b'Asian'), (1, b'Indian'), (2, b'African Americans'), (3, b'Asian Americans'), (4, b'European'), (5, b'British'), (6, b'Jewish'), (7, b'Latino'), (8, b'Native American'), (9, b'Arabic')])),
                ('weight', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('height', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('veg', models.BooleanField(default=True)),
                ('drink', models.BooleanField(default=False)),
                ('dob', models.DateField(null=True)),
            ],
            options={
                'ordering': ['pnum'],
            },
        ),
    ]
