# Generated by Django 4.1.1 on 2022-09-28 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_job_delete_volunteer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='job',
            new_name='joblist',
        ),
    ]
