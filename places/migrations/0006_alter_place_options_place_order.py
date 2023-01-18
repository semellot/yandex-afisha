# Generated by Django 4.1.5 on 2023-01-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='place',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]