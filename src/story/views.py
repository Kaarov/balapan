from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import StoryListSerializer, StoryRetrieveSerializer
from .models import Story


class StoryListAPIView(generics.ListAPIView):
    serializer_class = StoryListSerializer
    queryset = Story.objects.all()


class StoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = StoryRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        story = Story.objects.filter(id=kwargs.get('pk'))
        if story:
            serializer = self.get_serializer(story.last(), data=request.data, partial=True)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("", status=status.HTTP_400_BAD_REQUEST)
