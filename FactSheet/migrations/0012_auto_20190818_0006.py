# Generated by Django 2.2.3 on 2019-08-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactSheet', '0011_auto_20190817_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_description',
            name='massage',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Массаж'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='room_type_max_pax',
            field=models.CharField(blank=True, max_length=200, verbose_name='Макс. размещение (взр.+реб)'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='total_room_numbers',
            field=models.FloatField(blank=True, null=True, verbose_name='Общее количество номеров'),
        ),
    ]