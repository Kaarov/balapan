from django.urls import path
from .views import StoryListAPIView, StoryRetrieveAPIView

urlpatterns = [
    path('story/', StoryListAPIView.as_view(), name='story'),
    path('story/<int:pk>/', StoryRetrieveAPIView.as_view(), name='story_retrieve'),
]
