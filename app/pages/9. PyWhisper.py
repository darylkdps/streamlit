# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st
import pywhisper
import torch
# import numpy as np
# from datetime import timedelta
# from PIL import Image
from pathlib import Path
from tempfile import NamedTemporaryFile
# import time
# import os


st.title('Audio Transcription and Translation PyWhisper')

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
if DEVICE == 'cuda':
    st.text('Using GPU')
else:
    st.text('Using CPU')


performance = st.select_slider(
    'Select performance',
    options=('Very Fast', 'Fast', 'Balanced', 'Accurate', 'Very Accurate'),
    value='Fast'
    )

match performance:
    case 'Very Fast':
        model_size = 'tiny'

    case 'Fast':
        model_size = 'base'

    case 'Balanced':
        model_size = 'small'

    case 'Accurate':
        model_size = 'medium'

    case 'Very Accurate':
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

        model = pywhisper.load_model(model_size, device=DEVICE)
        result = model.transcribe(audio=tempFile.name, verbose=True)
        st.write(result["text"])