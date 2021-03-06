# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwords', '0007_auto_20160906_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learnstate',
            old_name='user',
            new_name='userproperty',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='userproperty',
        ),
        migrations.AlterUniqueTogether(
            name='learnstate',
            unique_together=set([('userproperty', 'word')]),
        ),
    ]
