from django.urls import path
from .views import CategoryListAPIView
from .views import WordRetrieveAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('word/<int:pk>/', WordRetrieveAPIView.as_view(), name='word'),
]
