# Generated by Django 2.1.4 on 2018-12-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0004_auto_20181220_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='component',
            name='usage',
            field=models.IntegerField(choices=[(1, 'шт'), (2, 'кг')], default=2),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measure',
            field=models.PositiveIntegerField(choices=[(1, 'кг'), (2, 'г'), (3, 'шт'), (4, 'л')], default=1),
        ),
    ]
