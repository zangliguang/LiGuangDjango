# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import liguang_first.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('business_id', liguang_first.models.UUIDField(max_length=64, serialize=False, editable=False, primary_key=True, blank=True)),
                ('business_name', models.CharField(max_length=16)),
                ('business_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BusinessClass',
            fields=[
                ('businessclass_id', liguang_first.models.UUIDField(max_length=64, serialize=False, editable=False, primary_key=True, blank=True)),
                ('businessclass_name', models.CharField(max_length=16)),
                ('businessclass_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='businessclass_id',
            field=models.ForeignKey(to='liguang_first.BusinessClass'),
        ),
    ]
