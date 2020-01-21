from rest_framework import serializers


class AdvertisementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    createAt = serializers.DateTimeField()
    price = serializers.IntegerField()
    category = serializers.CharField()

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
