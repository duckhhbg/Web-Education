# Generated by Django 4.2 on 2023-04-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timer', models.IntegerField(default=0)),
                ('Couter', models.IntegerField(default=0)),
            ],
        ),
    ]
