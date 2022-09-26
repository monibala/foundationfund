# Generated by Django 3.2.9 on 2021-11-17 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couses', '0005_alter_couses_category'),
        ('events', '0003_eventimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Events', to='couses.category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
