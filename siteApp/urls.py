from django.conf.urls import re_path
from .views import AdvertisementView


app_name = "advertisements"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    re_path('advertisements/', AdvertisementView.as_view()),
    re_path('advertisements/<int:pk>', AdvertisementView.as_view()),
]