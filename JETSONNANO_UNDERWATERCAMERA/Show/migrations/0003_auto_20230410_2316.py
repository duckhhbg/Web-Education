# Generated by Django 3.2.7 on 2023-04-10 16:16

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0002_rename_auto_auto_camera_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto_camera',
            options={'verbose_name_plural': 'Auto Cameras'},
        ),
        migrations.RenameField(
            model_name='auto_camera',
            old_name='Couters',
            new_name='Counters',
        ),
        migrations.AddField(
            model_name='auto_camera',
            name='start_Time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auto_camera',
            name='stat_Date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
