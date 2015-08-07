# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liguang_first', '0004_auto_20150807_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_contentss',
            new_name='business_contents',
        ),
    ]
