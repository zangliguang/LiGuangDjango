# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liguang_first', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='businessclass_id',
            new_name='businessclass',
        ),
    ]
