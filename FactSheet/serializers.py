from rest_framework import serializers
from . import models
from .forms import SuperHotelForm

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel_description
        fields = ('id', 'hotel_name', 'category', 'text_block', 'email_block', 'hotel_images', 'square', 'adress', 'telephone', 'web_site',
                  'distance_to_center', 'nearest_airport', 'distance_to_airport', 'distance_to_beach', 'construction_year',
                  'renovation_year', 'meal', 'check_in', 'check_out', 'deposit', 'credit_card', 'credit_card_other',
                  'main_building', 'anex_quantity', 'anex_floors', 'villas_quantity', 'villas_floors', 'other_buildings_quantity',
                  'other_buildings_floors', 'disabled', 'pets_friendly', 'non_smoking_hotel', 'adults_only', 'adults_only_age',
                  'nanny', 'child_chairs', 'child_food', 'child_playground', 'baby_cot', 'child_carriage', 'baby_equipment',
                  'mother_corner', 'child_restaurant', 'child_club', 'child_club_age', 'child_pool', 'child_pool_quantity',
                  'total_room_numbers', 'room_type_name', 'room_type_numbers', 'room_type_building', 'room_type_view',
                  'room_type_view_other', 'room_type_view_other', 'room_type_size', 'room_type_beds', 'room_type_beds_other',
                  'connected_rooms', 'door_rooms', 'living_room', 'room_type_max_pax', 'room_type_extra_beds', 'room_type_rooms',
                  'room_type_bedrooms', 'room_type_areas', 'shower', 'hair_dryer', 'roba_and_slippers', 'jakuzi', 'mini_kitchen',
                  'dishes', 'oven', 'dishwasher', 'microwave', 'air_condition', 'coffee_and_tea', 'ketler', 'mini_bar',
                  'fridge', 'tv', 'dvd', 'telephone_in_room', 'tv_channels', 'wi_fi', 'wi_fi_price', 'safe', 'safe_price',
                  'balcony', 'terrace', 'carpet', 'room_clenaning', 'bed_linen_changing', 'towel_changing', 'ironing',
                  'room_service', 'shower', 'hair_dryer', 'roba_and_slippers', 'jakuzi', 'mini_kitchen', 'dishes', 'oven',
                  'dishwasher', 'microwave', 'air_condition', 'coffee_and_tea', 'ketler', 'mini_bar', 'fridge', 'tv', 'dvd',
                  'telephone_in_room', 'tv_channels', 'wi_fi', 'wi_fi_price', 'safe', 'safe_price', 'balcony', 'terrace',
                  'carpet', 'room_clenaning', 'bed_linen_changing', 'towel_changing', 'ironing', 'room_service', 'beach_location',
                  'beach_shattle', 'beach_location_m', 'beach_type', 'beach_sand', 'beach_length', 'beach_towels', 'beach_towels_price',
                  'beach_umbrella', 'beach_umbrella_price', 'beach_mattres', 'beach_mattres_price', 'beach_chaise_lounge',
                  'beach_chaise_lounge_price', 'beach_gazebo', 'beach_gazebo_price', 'restaurant_quntity', 'main_restaurant_cusine',
                  'main_restaurant_working_hours', 'a_la_carte_quntity', 'a_la_carte_free_quntity', 'a_la_carte_restaurant_cusine',
                  'bar_quntity', 'bar_choice', 'bar_pool', 'bar_beach', 'bar_cusine', 'continental_breakfact', 'buffet_breakfast',
                  'late_breakfast', 'lunch_buffet', 'menu_lanch', 'sandwich_corner', 'coffee_and_desserts', 'dinner_buffet',
                  'dinner_menu', 'late_dinner', 'night_snacks', 'snacks_24_h', 'ice_cream', 'fresh', 'soft_drinks', 'local_alkohol_drinks',
                  'imported_drinks', 'barbeku', 'all_inclusive_working_hours', 'all_inclusive_pay', 'all_inclusive_mini_bar',
                  'all_inclusive_mini_bar_choice', 'aerobics', 'aquaaerobics', 'basketball', 'football', 'volleyboll', 'bocce',
                  'mini_football', 'golf', 'gym', 'tennis_cort', 'table_tennis', 'animation', 'children_animation', 'live_music',
                  'water_sport', 'bicykle_rent', 'billiard', 'bowling', 'casino', 'katamarans', 'cinema', 'disco', 'diving',
                  'videogames', 'jacuzzi', 'night_club', 'serfing', 'water_polo', 'tennis_equipment', 'spa', 'massage',
                  'spa_treatment', 'outdoor_swimming_pool', 'outdoor_swimming_pool_heating', 'outdoor_swimming_pool_for_children',
                  'outdoor_swimming_pool_with_sea_water', 'indoor_swimming_pool', 'indoor_swimming_pool_heating', 'indoor_swimming_pool_for_children',
                  'indoor_swimming_pool_with_sea_water', 'aquapark', 'water_slides', 'beauty_salon', 'hair_dresser', 'shop',
                  'laundry', 'amphiteatre', 'atm', 'exchange', 'parking', 'library', 'conference_room', 'conference_room_quantity',
                  'wi_fi_in_hotel', 'wi_fi_in_hotel_price', 'reception_safe', 'reception_safe_price', )