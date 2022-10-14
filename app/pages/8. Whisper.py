# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st
import whisper
import torch
import numpy as np
from datetime import timedelta
from PIL import Image
from pathlib import Path
from tempfile import NamedTemporaryFile
import time

st.title('Audio Transcription and Translation')

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
    return whisper.load_model(model_size, device=DEVICE)

# audio = st.file_uploader('Upload an audio file', type=['mp3', 'aac', 'wav'])
audio = st.file_uploader('Upload an audio file', type=['aac'])

tempFile = NamedTemporaryFile()
try:
    tempFile.write(audio.getvalue())
    tempFile.seek(0)

    # audio_bytes = uploaded_file.read()
    st.audio(audio.getvalue(), format='audio/aac')

    f = 'D:\Script\Christine DA 2020 (3 min).aac'
    model = whisper.load_model('base')
    result = model.transcribe(audio=tempFile.name)
    st.write(result["text"])
finally:
    tempFile.close()




# if audio is not None:
#     ext = Path(audio.name).suffix
#     ext

#     with NamedTemporaryFile(suffix='aac') as tempFile:
#         tempFile.write(audio.getvalue())
#         tempFile.seek(0)
#         st.text(tempFile.name)

#         # time.sleep(30)

#         # model = load_model()
#         model = whisper.load_model('base')
#         result = model.transcribe(audio=tempFile.name)
#         st.write(result["text"])



#  tempfile.NamedTemporaryFile(mode='w+b', buffering=- 1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)¶





# if uploaded_file is not None:
#     st.text(uploaded_file.name)

#     # image = Image.open(uploaded_file)
#     # st.image(image, caption='Sunrise by the mountains')

#     # uploaded_file
#     # uploaded_file.read()
#     # uploaded_file.getvalue()
#     # uploaded_file.getvalue().decode('utf-8')


#     bytes_data = uploaded_file.getvalue().decode('utf-8')

#     # audio_file = open(uploaded_file, 'r')
#     audio_bytes = uploaded_file.read()
#     st.audio(audio_bytes, format='audio/aac')

#     model = load_model()

#     audio = whisper.load_audio(file=bytes_data)
#     audio = whisper.pad_or_trim(audio)
#     mel = whisper.log_mel_spectrogram(audio).to(model.device)
#     options = whisper.DecodingOptions(language='en', without_timestamps=False, fp16=False)
#     result = whisper.decode(model, mel, options)


#     result = model.transcribe(audio=bytes_data, verbose=True, fp16=False)
#     st.text(result["text"])



