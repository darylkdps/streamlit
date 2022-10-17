import streamlit as st
import pywhisper
import torch
from pathlib import Path
from tempfile import NamedTemporaryFile
from datetime import timedelta

st.title('Audio Transcription and Translation PyWhisper')

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
if DEVICE == 'cuda':
    st.text('Using GPU')
else:
    st.text('Using CPU')

performance_values = ('Very fast', 'Fast', 'Balanced but slow', 'Accurate but slower', 'Very Accurate and very very slow')

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

@st.cache(allow_output_mutation=True)
def load_model(model_size=model_size):
    st.write('Using ' + model_size + ' model')
    return pywhisper.load_model(model_size, device=DEVICE)

@st.cache(allow_output_mutation=True)
def load_file(audio):    
    return audio


audio = st.file_uploader('Upload an audio file', type=['mp3', 'aac', 'wav'])
if audio is not None:
    ext = Path(audio.name).suffix[1:]
    
    with NamedTemporaryFile(suffix=ext) as tempFile:
        tempFile.write(load_file(audio).getvalue())
        tempFile.seek(0)

        st.write('File name: ' + audio.name)        
        st.write('File extension: ' + ext)

        st.audio(tempFile.read(), format='audio/' + ext)

        with st.spinner('Transcribing ...'):

            model = pywhisper.load_model(model_size, device=DEVICE)
            result = model.transcribe(audio=tempFile.name, verbose=False)
        
        st.success('Done')

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