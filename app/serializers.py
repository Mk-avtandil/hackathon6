from rest_framework import serializers
from .models import *


class NewsDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'