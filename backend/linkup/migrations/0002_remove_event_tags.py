# Generated by Django 4.0.5 on 2022-09-04 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
    ]
