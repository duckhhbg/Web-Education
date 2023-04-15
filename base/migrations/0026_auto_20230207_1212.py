# Generated by Django 3.2.7 on 2023-02-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_subject_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='access',
            field=models.CharField(choices=[('Cơ bản', 'Cơ bản'), ('Cơ sở', 'Cơ sở'), ('Chuyên ngành', 'Chuyên ngành')], default='Cơ bản', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.CharField(choices=[('SV', 'SV'), ('GV', 'GV'), ('AD', 'AD')], default='SV', max_length=2),
        ),
    ]
