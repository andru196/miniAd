from rest_framework import serializers
from .models import Photo, Advertisement
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PhotoSerializer(serializers.Serializer):
    url = serializers.SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        if obj is not None:
            return self.context['request'].build_absolute_uri(obj.image.url)


class AdvertisementListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    photo = serializers.SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        if obj.photo is not None:
            return self.context['request'].build_absolute_uri(obj.photo.image.url)


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'price', 'photos', 'id', 'user', 'description', 'createAt', 'category')
    id = serializers.IntegerField()
    user = UserSerializer()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    createAt = serializers.DateTimeField()
    price = serializers.IntegerField()
    category = serializers.CharField()
    photos = PhotoSerializer(many=True)

    def get_photo_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image)

    def create(self, validated_data):
        return AdvertisementSerializer.objects.create(**validated_data)

    def __init__(self, *args, **kwargs):
        super(serializers.Serializer, self).__init__(*args, **kwargs)
        if 'context' in kwargs and 'fields_list' in kwargs['context']:
            fields_list = kwargs['context']['fields_list']
            fields_list = set(fields_list)
            for field in set(self.fields) - fields_list:
                self.fields.pop(field)
