from rest_framework import serializers
from .models import Photo, Advertisement
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['url', 'link']
        read_only_fields = ['link']

    url = serializers.URLField(write_only=True)
    link = serializers.SerializerMethodField('get_photo_url', read_only=True)

    def get_photo_url(self, obj):
        if obj is not None and obj.image is not None and obj.image != '':
            return self.context['request'].build_absolute_uri(obj.image.url)
        elif obj is not None:
            return obj.url


class AdvertisementListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    photo = serializers.SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        if obj.photo is not None and obj.photo.image is not None and obj.photo.image != '':
            return self.context['request'].build_absolute_uri(obj.photo.image.url)
        elif obj.photo is not None:
            return obj.photo.url


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'price', 'photos', 'id', 'user', 'description', 'createAt', 'category')
    id = serializers.IntegerField(required=False)
    user = UserSerializer(required=False)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    createAt = serializers.DateTimeField(required=False)
    price = serializers.IntegerField()
    category = serializers.CharField(required=False)
    photos = PhotoSerializer(many=True, required=False)

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        ad = Advertisement.objects.create(**validated_data)
        for url in photos_data:
            photo = Photo.objects.create(**url, ad=ad)
            photo.save()
        return ad

    def __init__(self, *args, **kwargs):
        super(serializers.Serializer, self).__init__(*args, **kwargs)
        if 'context' in kwargs and 'fields_list' in kwargs['context']:
            fields_list = kwargs['context']['fields_list']
            fields_list = set(fields_list)
            for field in set(self.fields) - fields_list:
                self.fields.pop(field)
