from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer

# Create your views here.

class ListVideo(APIView):
    def get(self, request):
        videos = Video.objects.all()
        video_json = VideoSerializer(videos, many=True)
        return Response(video_json.data)


