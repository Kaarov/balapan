from rest_framework import serializers

from .models import Story, TextModel


class StoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ("id", "title", "image", "file")


class TextModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextModel
        fields = ('title', )


class StoryRetrieveSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField('get_text')

    class Meta:
        model = Story
        fields = ("id", "title", "image", "file", "text")

    def get_text(self, story):
        text = TextModel.objects.filter(story=story)
        return TextModelSerializer(text, many=True).data
