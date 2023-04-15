# Generated by Django 3.2.7 on 2022-12-22 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_subject_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.IntegerField(choices=[('SV', 'Student'), ('GV', 'Teacher'), ('AD', 'Admin')], default=0),
        ),
    ]
