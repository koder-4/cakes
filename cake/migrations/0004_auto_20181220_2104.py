# Generated by Django 2.1.4 on 2018-12-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_auto_20181220_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cake',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='component',
            name='version',
            field=models.PositiveIntegerField(default=1),
        ),
    ]