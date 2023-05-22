# Whisper API and Diarization Sample Code

from openai require import Client
client = Client('your-openai-api-key')

def transcribe(audio_file):
    with open(audio_file, 'rb') as f:
        audio = f.read()
    response = client.whisper.transcribe(audio_data=audio)
    return response

def diarize(transcript):
    diarization = []
    for word in transcript['words]:
        if 'speaker' in word:
            diarization.append({'start': word['start'], 'end': word['end'], 'speaker': word['speaker']})
    return diarization
