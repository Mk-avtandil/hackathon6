from rest_framework import serializers
from .models import *


class NewsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class VideoDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'