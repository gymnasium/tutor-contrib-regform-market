# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True,
                )),
                ('market', models.CharField(
                    blank=True,
                    max_length=5,
                    verbose_name=b'Select Nearest Region',
                    choices=[(b'Venus', b'01'), (b'Mars', b'02')],
                )),
                ('user', models.OneToOneField(
                    on_delete=models.CASCADE,
                    null=True,
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
        ),
    ]
