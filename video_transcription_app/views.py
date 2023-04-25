import pytube
import subprocess
from pydub import AudioSegment
import speech_recognition as speech

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from video_transcription_app.models import Video

@csrf_exempt
def transcribe_video(request):
    if request.method == 'POST':

        video_url = request.POST.get('video_url')

        video_file = 'video.mp4'
        audio_file = 'audio.wav'
        
        with open(audio_file, 'w') as file:
            ...

        video_date = pytube.YouTube(video_url)
        stream = video_date.streams.get_highest_resolution()
        stream.download(filename="video.mp4")

        subprocess.run(['ffmpeg', '-i', video_file, '-f', 'wav', audio_file])
        
        audio = AudioSegment.from_wav(audio_file)

        rec = speech.Recognizer()
        with speech.AudioFile(audio_file) as source:
            audio = rec.record(source)
        transcript = rec.recognize_google(audio)

        video = Video.objects.create(video_url=video_url, transcript=transcript)
        video.save()

        return JsonResponse({'message': transcript})