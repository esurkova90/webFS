# Generated by Django 2.2.3 on 2019-08-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactSheet', '0006_auto_20190813_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_description',
            name='room_type_bedrooms',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество спален'),
        ),
    ]
