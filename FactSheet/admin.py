from django.contrib import admin

from .models import Hotel_description

from .urls import urlpatterns

admin.site.register(Hotel_description)
