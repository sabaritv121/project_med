# Generated by Django 4.2.10 on 2024-04-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mediassist_app', '0005_medicine_approval_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine_request',
            name='prescription',
            field=models.FileField(blank=True, null=True, upload_to='pic/'),
        ),
    ]
