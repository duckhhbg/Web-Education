# Generated by Django 3.2.7 on 2022-12-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_chapter_fksubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='url',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='video',
            field=models.FileField(default=None, null=True, upload_to='videos'),
        ),
    ]
