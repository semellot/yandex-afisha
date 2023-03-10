# Generated by Django 3.2.16 on 2023-01-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('sort', models.IntegerField(verbose_name='Сортировка')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Место')),
            ],
        ),
    ]
