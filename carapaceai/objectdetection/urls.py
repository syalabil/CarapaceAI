from django.urls import path
from .views import * 

app_name = 'objectdetection'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('livefeed/',LiveCameraView.as_view(), name="live-feed" ),
    path('upload/', upload_video_file),
]