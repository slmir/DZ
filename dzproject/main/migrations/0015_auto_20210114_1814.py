# Generated by Django 3.1.5 on 2021-01-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210113_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foldnewone',
            name='square',
            field=models.IntegerField(verbose_name='Площадь склада'),
        ),
    ]
