from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from .models import Hotel_description
from tkinter import *
import requests
from . import forms
from .forms import SuperHotelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django_filters


def index(request):
    if request.method == "POST":
        form = SuperHotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Отель добавлен. Спасибо!")
        else:
            return HttpResponse(f"Ошибочки {form.errors}. Спасибо!")
    else:
        form = SuperHotelForm()
        return render(request, "FactSheet/wrapper.html", {"form": form})


from rest_framework import viewsets
from . import serializers
from . import models

class HotelsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HotelSerializer
    queryset = models.Hotel_description.objects.all()
