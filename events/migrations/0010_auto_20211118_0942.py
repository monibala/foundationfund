# Generated by Django 3.2.9 on 2021-11-18 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_events_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eventEndTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='host',
            field=models.CharField(default='Cyberflax PVT LTD', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='topics',
            field=models.CharField(default='Children around the world are not enrolled in school', max_length=200),
            preserve_default=False,
        ),
    ]
