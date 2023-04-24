from django.urls import path
from . import views

urlpatterns = [
    path('transcribe_video', views.transcribe_video, name='transcribe_video'),
]