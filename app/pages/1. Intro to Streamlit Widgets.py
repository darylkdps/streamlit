# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st

## Lesson 1 Start ##################################################

# Create title
st.title('1. Test of Streamlit Widgets')

# Create text
st.write('This is my new app2')

# Create a button
button1 = st.button('Click Me')

if button1:
    # if button1 is clicked
    st.write('This is some text that appears when you click "Click Me".')

like = st.checkbox('Do you like this app?')

button2 = st.button('Submit')

# if button2:
#     # if button2 is clicked
#     st.write(like)

if button2:
    # if button2 is clicked
    if like:
        # if like is checked
        st.write('Thanks. I like it too.')
    else:
        # if like is not checked
        st.write("I'm sorry.")

st.header('Start of the Radio Button Section')

animal = st.radio('What animal is your favourite?', ('Lion', 'Tiger', 'Bear') )

button3 = st.button('Submit Animal')

if button3:
    # if button3 is clicked
    st.write(animal)
    if animal == 'Lion':
        st.write('Roar')

st.header('Start of the Selectbox Section')

animal2 = st.selectbox('What animal is your favourite?', ('Lion', 'Tiger', 'Bear') )  # returns str

button4 = st.button('Submit Animal2')  # button labels must be unique

if button4:
    # if button4 is clicked
    st.write(animal2)
    if animal2 == 'Lion':
        st.write('Roar')

st.header('Start of the Multiselect Section')

options = st.multiselect('What animals do you like?', ('Lion', 'Tiger', 'Bear'))  # returns list

button5 = st.button('Print Animals')

if button5:
    st.write(options)

st.header('Start of the Slider Section')

epochs_num = st.slider('How many epochs?', 1, 100, 10)

if st.button('Slider Button'):
    st.write(epochs_num)

st.header('Start of the Text Input Section')

user_text = st.text_input('What is your favourite movie?', 'Star Trek')

if st.button('Text Button'):
    st.write(user_text)
    # st.write(int(user_text))

user_num = st.number_input('What is your favourite number?')

if st.button('Number Button'):
    st.write(user_num)

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')

def run_sentiment_analysis(txt):
    st.write(f'Analysis Done: {txt}')

st.write('Sentiment:', run_sentiment_analysis(txt))

## Lesson 1 Ends