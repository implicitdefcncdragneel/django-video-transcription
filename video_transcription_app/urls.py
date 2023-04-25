from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcribe_video, name='transcribe_video'),
]