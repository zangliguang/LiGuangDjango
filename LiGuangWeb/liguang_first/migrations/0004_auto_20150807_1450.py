# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liguang_first', '0003_auto_20150807_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_contents',
            new_name='business_contentss',
        ),
    ]
