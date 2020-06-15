from django.urls import path
from .views import ListVideo,DetailVideo

#EndPoint
urlpatterns = [
    path('videos/',ListVideo.as_view(),name='lista-video'),
    path('videos/<int:pk>/',DetailVideo.as_view(),name='lista-video'),
]
