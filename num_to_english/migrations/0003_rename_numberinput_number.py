# Generated by Django 4.2.8 on 2023-12-08 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('num_to_english', '0002_numberinput_delete_convertednumber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NumberInput',
            new_name='Number',
        ),
    ]
