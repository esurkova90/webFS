# Generated by Django 2.2.3 on 2019-08-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactSheet', '0007_auto_20190813_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_description',
            name='a_la_carte_free_quntity',
            field=models.FloatField(blank=True, null=True, verbose_name='Из них бесплатных'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='a_la_carte_quntity',
            field=models.FloatField(blank=True, null=True, verbose_name='Кол-во A la Carte'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='main_restaurant_working_hours',
            field=models.TimeField(blank=True, null=True, verbose_name='Главный ресторан, часы работы'),
        ),
    ]