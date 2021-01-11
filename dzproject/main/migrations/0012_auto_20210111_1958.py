# Generated by Django 3.1.5 on 2021-01-11 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210111_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoldNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название склада')),
                ('parknumber', models.IntegerField(verbose_name='Номер платформы')),
                ('responsible', models.CharField(blank=True, max_length=50, verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='ItemNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('category', models.CharField(choices=[('Мебель', 'Мебель'), ('Стройматериалы', 'Строительные материалы'), ('Инструменты', 'Инструменты для выполнения строительных,отделочных работ'), ('Техника', 'Технические средства, машины для строительных, отделочных работ')], max_length=50, verbose_name='Категория')),
                ('amount', models.IntegerField(verbose_name='Количество')),
                ('shelflifeday', models.IntegerField(verbose_name='Дней хранения')),
                ('option', models.TextField(blank=True, verbose_name='Описание')),
                ('foldid', models.ForeignKey(blank='True', on_delete=django.db.models.deletion.CASCADE, to='main.foldnew', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='foldid',
        ),
        migrations.DeleteModel(
            name='Fold',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
