from django.conf.urls import re_path
from django.urls import path
from .views import AdvertisementView, AdvertisementManyView


app_name = "advertisements"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('advertisements/<int:pageN>', AdvertisementManyView.as_view()),
    #re_path('advertisement/<int:adID>', AdvertisementView.as_view()),
    #re_path('advertisement', AdvertisementView.as_view()),
]