# Generated by Django 3.2.6 on 2021-12-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211223_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='unitcode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='exams',
            name='unitcode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notes',
            name='unitcode',
            field=models.CharField(max_length=50),
        ),
    ]