# Generated by Django 4.2.10 on 2024-04-27 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mediassist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='adhar_number',
            new_name='register_number',
        ),
        migrations.RemoveField(
            model_name='users',
            name='blood_group',
        ),
    ]
