from django.urls import path
from .views import ListVideo

#EndPoint
urlpatterns = [
    path('videos/',ListVideo.as_view(),name='lista-video'),
]
