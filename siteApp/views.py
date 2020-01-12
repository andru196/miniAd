# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdvertisementSerializer


class AdvertisementView(APIView):
    def get(self, request):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response({"advertisements": serializer.data})
# Create your views here.
