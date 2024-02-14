from rest_framework.response import Response
from rest_framework import generics, status

from .models import Category, Word
from .serializers import CategoryListSerializer
from .serializers import WordRetrieveSerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class WordRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WordRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        category = Category.objects.filter(id=kwargs.get('pk'))
        if category:
            serializer = self.get_serializer(category.last(), data=request.data, partial=True)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("", status=status.HTTP_400_BAD_REQUEST)
