# Generated by Django 4.0.6 on 2022-11-24 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_information_enter_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='information',
            new_name='field_name',
        ),
    ]
