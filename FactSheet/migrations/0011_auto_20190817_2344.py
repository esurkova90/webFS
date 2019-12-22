# Generated by Django 2.2.3 on 2019-08-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactSheet', '0010_auto_20190816_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_description',
            name='air_condition',
            field=models.CharField(blank=True, choices=[('центральное кондиционирование', 'центральное кондиционирование'), ('индивидуальный кондиционер', 'индивидуальный кондиционер'), ('вентилятор', 'вентилятор'), ('сплит-система', 'сплит-система'), ('без кондиционера', 'без кондиционера')], max_length=120, verbose_name='Кондиционер'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='aquapark',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Аквапарк'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='baby_cot',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Детская кроватка в номере'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='baby_equipment',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Горшок, ванна, подогреватель бутылочек'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='balcony',
            field=models.CharField(blank=True, choices=[('балкон', 'балкон'), ('французский балкон', 'французский балкон')], max_length=120, verbose_name='Балкон'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='bar_choice',
            field=models.CharField(blank=True, choices=[('бар на пляже', 'бар на пляже'), ('бар у бассейна', 'бар у бассейна'), ('лобби-бар', 'лобби-бар'), ('кафе-бар', 'кафе-бар'), ('диско-бар', 'диско-бар'), ('витамин-бар', 'витамин-бар')], max_length=120, verbose_name='Бары'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_chaise_lounge',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Шезлонги'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_gazebo',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Газебо'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_location',
            field=models.CharField(blank=True, choices=[('первая линия', 'первая линия'), ('через дорогу', 'через дорогу'), ('вторая линия', 'вторая линия'), ('шаттл-бас до пляжа', 'шаттл-бас до пляжа')], max_length=120, verbose_name='Расположение пляжа'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_mattres',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Матрасы'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_sand',
            field=models.CharField(blank=True, choices=[('песок', 'песок'), ('галька', 'галька'), ('песчано-галечный', 'песчано-галечный')], max_length=120, verbose_name='Покрытие пляжа'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_towels',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Пляжные полотенца'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_type',
            field=models.CharField(blank=True, choices=[('частный', 'частный'), ('публичный', 'публичный')], max_length=120, verbose_name='Частный/публичный'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='beach_umbrella',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Пляжные зонты'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='bicykle_rent',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Аренда велосипедов'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='billiard',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Бильярд'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='bowling',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Боулинг'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='carpet',
            field=models.CharField(blank=True, choices=[('ковер', 'ковер'), ('керамика', 'керамика'), ('ламинат', 'ламинат'), ('паркет', 'паркет')], max_length=120, verbose_name='Покрытие пола'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='casino',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Казино'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='category',
            field=models.CharField(blank=True, choices=[('3* ', '3* '), ('4* ', '4* '), ('5* ', '5* '), ('- ', '- ')], max_length=150, verbose_name='Звездность'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_carriage',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Детская коляска'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_chairs',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Высокие стулья в ресторане'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_club',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Детский клуб'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_food',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Детское меню'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_playground',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Детская площадка'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_pool',
            field=models.CharField(blank=True, choices=[('есть', 'есть'), ('нет', 'нет')], max_length=150, verbose_name='Детский бассейн'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='child_restaurant',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Детский ресторан'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='cinema',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Кинотеатр'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='conference_room',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Конференц-зал'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='credit_card',
            field=models.CharField(blank=True, choices=[('Visa', 'Visa'), ('Master Card', 'Master Card'), ('Dinners', 'Dinners'), ('Другое (укажите)', 'Другое (укажите)')], max_length=150, verbose_name='Кредитные карты'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='disco',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Дискотека'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='diving',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Дайвинг'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='ironing',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Утюг и гладильная доска'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='jacuzzi',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Джакузи'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='katamarans',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Аренда катамаранов'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='massage',
            field=models.CharField(choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Массаж'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='meal',
            field=models.CharField(blank=True, choices=[('BB', 'BB'), ('HB', 'HB'), ('FB', 'FB'), ('All Inclusive', 'All Inclusive')], max_length=50, verbose_name='Тип питания'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='mother_corner',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Уголок матери'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='nanny',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=150, verbose_name='Услуги няни'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='night_club',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Ночной клуб'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='reception_safe',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Сейф на ресепшен'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='room_service',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Сервис в номер'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='room_type_beds',
            field=models.CharField(blank=True, choices=[('Double French Bed', 'Double French Bed'), ('Double King Size Bed', 'Double King Size Bed'), ('Twin bed', 'Twin bed'), ('Другое', 'Другое')], max_length=200, verbose_name='Тип кровати'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='room_type_building',
            field=models.CharField(blank=True, choices=[('Главное здание', 'Главное здание'), ('Anex', 'Anex'), ('Villa', 'Villa'), ('Бунгало', 'Бунгало'), (6, 'Доп корпус')], max_length=120, verbose_name='В каком здании номер'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='room_type_extra_beds',
            field=models.CharField(blank=True, choices=[('Normal Bed', 'Normal Bed'), ('Pull Out Chair', 'Pull Out Chair'), ('Pull Out Couch', 'Pull Out Couch'), ('Sofa', 'Sofa'), ('нет', 'нет')], max_length=120, verbose_name='Доп место для ребенка'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='room_type_view',
            field=models.CharField(blank=True, choices=[('Sea View', 'Sea View'), ('Pool View', 'Pool View'), ('Garden View', 'Garden View'), ('Другое', 'Другое')], max_length=120, verbose_name='Вид из номера'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='safe',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Сейф'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='serfing',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Серфинг'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='shower',
            field=models.CharField(blank=True, choices=[('душ', 'душ'), ('ванна', 'ванна'), ('душ и ванна', 'душ и ванна')], max_length=120, verbose_name='Душ/ванна'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='spa',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='SPA'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='tennis_equipment',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('освещение платно', 'освещение платно'), ('оборудование платно', 'оборудование платно')], max_length=120, verbose_name='Оборудование для тенниса'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='videogames',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Видеоигры'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='water_polo',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Водное поло'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='wi_fi',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Wi-Fi'),
        ),
        migrations.AlterField(
            model_name='hotel_description',
            name='wi_fi_in_hotel',
            field=models.CharField(blank=True, choices=[('бесплатно', 'бесплатно'), ('платно', 'платно')], max_length=120, verbose_name='Wi-Fi на территории'),
        ),
    ]
