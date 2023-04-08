from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('video_feed/', livefe, name='video_feed'),
    path('capture/', capture, name='capture'),
    path('getValue/', getValue, name="getValue")
]