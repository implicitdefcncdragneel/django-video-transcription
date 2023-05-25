import os
import pytube
import subprocess
from pydub import AudioSegment
import speech_recognition as speech

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from video_transcription_app.models import Video

@csrf_exempt
def transcribe_video(request):
    if request.method == 'POST':
        message = ""
        try:
            video_url = request.POST.get('video_url')

            video_file = 'video.mp4'
            audio_file = 'audio.wav'

            video_data = pytube.YouTube(video_url)
            stream = video_data.streams.get_highest_resolution()
            stream.download(filename="video.mp4")

            subprocess.run(['ffmpeg', '-i', video_file, '-f', 'wav', audio_file])

            audio = AudioSegment.from_wav(audio_file)

            rec = speech.Recognizer()
            with speech.AudioFile(audio_file) as source:
                audio = rec.record(source)
            transcript = rec.recognize_google(audio)

            video = Video.objects.create(video_url=video_url, transcript=transcript)
            video.save()
            message = transcript
            os.remove(video_file)
            os.remove(audio_file)
        except pytube.exceptions.PytubeError as e:
            message = "An error occurred while downloading the video: {}".format(str(e))
        except subprocess.CalledProcessError as e:
            message = "An error occurred while converting the video to audio: {}".format(str(e))
        except speech.UnknownValueError:
            message = "Error: Speech Recognition could not understand audio"
        except speech.RequestError as e:
            message = "Error: Could not request results from Speech Recognition service: {}".format(str(e))
        except Exception as e:
            # message = "An unexpected error occurred: {}".format(str(e))
            transcribe_video(request)
        context = {
            'message': message
        }
        return render(request, 'transcription_result.html', context)
    return render(request, 'transcribe_video.html')
