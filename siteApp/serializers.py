from rest_framework import serializers


class AdvertisementSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    createAt = serializers.DateTimeField()
    price = serializers.IntegerField()
    category = serializers.CharField()
