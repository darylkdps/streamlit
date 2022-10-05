# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st
# import spacy

# Lesson 5 Start  ##################################################

st.title('5. Session State')
# Session state addresses how the app is in fact re-started each time there is an interaction with a widget. 
# Session states helps provides an illusion of continuity in user interaction.

# counter = 0
# st.write(counter)

# if st.button('up'):
#     counter += 1
#     st.write(counter)

if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

st.write(st.session_state['counter'])

if st.button('up'):
    st.session_state['counter'] += 1
    st.write(st.session_state['counter'])

if st.button('reset'):
    st.session_state['counter'] = 0

# Lesson 5 Ends