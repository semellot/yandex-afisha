# Generated by Django 4.1.5 on 2023-01-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_placeimage_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Сортировка'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Сортировка'),
        ),
    ]
