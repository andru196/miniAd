# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.decorators import method_decorator

from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdvertisementSerializer, AdvertisementListSerializer
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin

class AdvertisementManyView(APIView):
    def get(self, request, pageN):
        if request.method == 'GET':
            sort_field = request.GET.get("sort")
            fields = map(lambda x: x.name, Advertisement._meta._get_fields())
            if sort_field not in fields:
                sort_field = None
        all_ads = Advertisement.objects.all().exclude(deleted=True).order_by('id' if sort_field is None else sort_field)
        current_page = Paginator(all_ads, 10)
        ad_list = []
        try:
            ad_list = current_page.page(pageN)
        except EmptyPage:
            return Response({"Error": "Страница не найдена"})

        for ad in ad_list:
            ad.photo = Photo.objects.filter(ad=ad).first()

        serializer = AdvertisementListSerializer(ad_list, many=True, context={'request': request})
        return Response({"advertisements": serializer.data})


class AdvertisementView(APIView, CsrfExemptMixin):
    authentication_classes = []

    def get(self, request, adID):
        if adID is None:
            return Response({"Error": "Не задан ID объявления"})

        advertisement = Advertisement.objects.get(id=adID)
        if advertisement is None:
            return Response({"Error": "  Объявадениене найденно"})

        advertisement.photos = Photo.objects.filter(ad=advertisement).order_by('id')
        enable_many_photo = bool(request.GET.get("photos"))
        if not enable_many_photo:
            advertisement.photos = advertisement.photos[0:1]

        fields = map(lambda x: x.name, Advertisement._meta._get_fields())

        extra_fields = str(request.GET.get("fields")).split(',')
        for extra in extra_fields:
            if extra not in fields:
                extra_fields.remove(extra)
        STANDART_FIELDS = ['title', 'price', 'photos']
        extra_fields = set(extra_fields)
        for field in STANDART_FIELDS:
            extra_fields.add(field)

        serializer = AdvertisementSerializer(advertisement, many=False,
                                        context={'request': request, 'fields_list': extra_fields, 'enable_many_photo': enable_many_photo})
        return Response({"advertisement": serializer.data})

    @csrf_exempt
    def post(self, request):
        article = request.data.get('advertisement')
        serializer = AdvertisementSerializer(data=article)
        code = '200'
        if serializer.is_valid():
            ad_saved = serializer.save()
            code = '201 Created'
        else:
            code = '500 Internal Server Error'
        return Response({"message":
                             {"Code": code, "AdvertisementId": ad_saved.id}})
