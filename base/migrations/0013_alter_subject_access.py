# Generated by Django 3.2.7 on 2022-12-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_subject_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='access',
            field=models.CharField(choices=[('Cơ bản', 'Cơ bản'), ('Cơ sở', 'Cơ sở'), ('Chuyên ngành', 'Chuyên ngành')], max_length=50),
        ),
    ]
