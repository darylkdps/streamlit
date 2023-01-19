import streamlit as st
import pywhisper
import torch
from pathlib import Path
from tempfile import NamedTemporaryFile
from datetime import timedelta

st.title('Audio Transcription and Translation PyWhisper2')

st.write('''This uses Open AI's Whisper, a neural network based automatic speech recognition, to transcribe or translate speech. It has 5 levels of speed-accuracy. Neural networks are, however, so big and computationally expensive that I have limited the options to just the smallest 3 to prevent crashing this app.''')

performance_values = ('Very fast', 'Fast', 'Balanced but slow')

performance = st.select_slider(
    'Select performance',
    options=performance_values,
    value='Fast'
    )

match performance:
    case 'Very fast':
        model_size = 'tiny'

    case 'Fast':
        model_size = 'base'

    case 'Balanced but slow':
        model_size = 'small'

    case 'Accurate but slower':
        model_size = 'medium'

    case 'Very Accurate and very very slow':
        model_size = 'large'

    case _:
        model_size = 'tiny'

audio = st.file_uploader('Upload an audio file', type=['mp3', 'aac', 'wav'])

if audio is not None:
    ext = Path(audio.name).suffix[1:]
    
    with NamedTemporaryFile(suffix=ext) as tempFile:
        tempFile.write(audio.getvalue())
        tempFile.seek(0)

        st.write('File name: ' + audio.name)
        st.write('File extension: ' + ext)

        st.audio(tempFile.read(), format='audio/' + ext)

        DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
            
        with st.spinner(f'Transcribing using {DEVICE} ...'):
            model = pywhisper.load_model(model_size, device=DEVICE)
            result = model.transcribe(audio=tempFile.name, verbose=False, fp16=False)
        
        st.success('Transcribed.')

        st.write(result["text"])
        st.write('Timestamped version:\n')

        tmpText = ''

        for segment in result['segments']:
            startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
            endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
            
            text = segment['text']
            segmentId = segment['id'] + 1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
            tmpText = tmpText + '\n' + segment
        
        st.text(tmpText)