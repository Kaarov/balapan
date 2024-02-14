from rest_framework import serializers

from .models import Category
from .models import Word


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "image")


class WordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ("id", "title", "image", "file")


class WordRetrieveSerializer(serializers.ModelSerializer):
    word = serializers.SerializerMethodField('get_word')

    class Meta:
        model = Category
        fields = ("id", "title", "image", "word")

    def get_word(self, category):
        word = Word.objects.filter(category=category)
        return WordListSerializer(word, many=True).data
