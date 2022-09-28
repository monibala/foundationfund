# Generated by Django 4.1.1 on 2022-09-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_remove_volunteer_volunteer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='volunteer',
        ),
    ]
