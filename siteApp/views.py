# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdvertisementSerializer
from rest_framework.generics import get_object_or_404


class AdvertisementView(APIView):
    def get(self, request):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response({"advertisements": serializer.data})

    def post(self, request):
        article = request.data.get('advertisement')
        serializer = AdvertisementSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            ad_saved = serializer.save()
        return Response({"success": "Advertisement '{}' created successfully".format(ad_saved.title)})

    def put(self, request, pk):
        saved_ad = get_object_or_404(Advertisement.objects.all(), pk=pk)
        data = request.data.get('advertisement')
        serializer = AdvertisementSerializer(instance=saved_ad, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ad_saved = serializer.save()
        return Response({
            "success": "Advertisement '{}' updated successfully".format(ad_saved.title)
        })

    def delete(self, request, pk):
        ad = get_object_or_404(Advertisement.objects.all(), pk=pk)
        ad.deleted = True
        ad.save()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)
