from django.conf.urls import url, include

from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('hotels', views.HotelsViewSet)


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^hotels/', include(router.urls)),
]