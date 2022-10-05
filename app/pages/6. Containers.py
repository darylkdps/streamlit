# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st

## Lesson 6 Start  ##################################################

st.title('6. Containers')
# Useful to maintain a widget's position if it needs to be updated using a later action.

main_container = st.container()

if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

if st.button('up'):
    main_container.write(st.session_state['counter'])
    # st.write(st.session_state['counter']) # will cause the counter to be written after the 'up' button
    st.session_state['counter'] += 1
    
if st.button('reset'):
    st.session_state['counter'] = 0

## Lesson 6 Ends