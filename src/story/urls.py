from django.urls import path
from .views import StoryListAPIView, StoryRetrieveAPIView

urlpatterns = [
    path('', StoryListAPIView.as_view(), name='story'),
    path('<int:pk>/', StoryRetrieveAPIView.as_view(), name='story_retrieve'),
]
