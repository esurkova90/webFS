# Generated by Django 2.2.3 on 2019-08-15 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactSheet', '0009_auto_20190816_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_description',
            name='category',
            field=models.CharField(blank=True, choices=[(1, '3* '), (2, '4* '), (3, '5* '), (4, '- ')], max_length=50, verbose_name='Звездность'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='meal',
            field=models.CharField(blank=True, choices=[(1, 'BB'), (2, 'HB'), (3, 'FB'), (4, 'All Inclusive')], max_length=50, verbose_name='Тип питания'),
        ),
    ]
