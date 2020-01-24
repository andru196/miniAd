from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class AdvertisementListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    photo = serializers.SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        if obj.photo is not None:
            return self.context['request'].build_absolute_uri(obj.photo)


class AdvertisementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    createAt = serializers.DateTimeField()
    price = serializers.IntegerField()
    category = serializers.CharField()
    photo = serializers.SerializerMethodField('get_photo_url')

    def get_photo_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.photo)

    def create(self, validated_data):
        return AdvertisementSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('user', instance.title)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.author_id = validated_data.get('price', instance.author_id)
        instance.title = validated_data.get('category', instance.title)
        instance.save()
        return instance
