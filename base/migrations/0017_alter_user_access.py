# Generated by Django 3.2.7 on 2023-01-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_subject_fkmajor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.CharField(choices=[('SV', 'SV'), ('GV', 'GV'), ('AD', 'AD')], default='SV', max_length=2),
        ),
    ]
