# Generated by Django 3.1.3 on 2020-11-28 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0002_auto_20201120_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-added_on']},
        ),
    ]
