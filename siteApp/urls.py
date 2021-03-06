from django.urls import path
from .views import AdvertisementView, AdvertisementManyView


app_name = "advertisements"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('advertisements/<int:pageN>', AdvertisementManyView.as_view()),
    path('advertisement/<int:adID>', AdvertisementView.as_view()),
    path('advertisement', AdvertisementView.as_view()),
]