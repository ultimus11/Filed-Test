from rest_framework import serializers
from .models import song
from .models import podcast
from .models import audiobook

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = '__all__'
class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = podcast
        fields = '__all__'
class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = audiobook
        fields = '__all__'