# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import User

def forwards_func(apps, schema_editor):
    if not User.objects.filter(username='root').exists():
        User.objects.create_superuser('root', None, 'root')


def reverse_func(apps, schema_editor):
    if User.objects.filter(username='root').exists():
        User.objects.get(username='root').delete()


class Migration(migrations.Migration):

    dependencies = [('links', '0002_auto_20170716_2315')]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
