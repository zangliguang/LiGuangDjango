# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liguang_first', '0002_auto_20150807_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_content',
            new_name='business_contents',
        ),
    ]
