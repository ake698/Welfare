# Generated by Django 3.1.7 on 2021-03-18 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210318_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='img',
        ),
    ]
