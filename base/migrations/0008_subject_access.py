# Generated by Django 3.2.7 on 2022-12-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20221220_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='access',
            field=models.IntegerField(choices=[(0, 'Cơ bản'), (1, 'Cơ sở'), (2, 'Chuyên ngành')], default=0),
        ),
    ]
