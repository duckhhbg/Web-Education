# Generated by Django 3.2.7 on 2022-12-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='fksubject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.subject'),
        ),
    ]
