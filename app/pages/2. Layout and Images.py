# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st

## Lesson 2 Start  ##################################################
st.title('2. Layout and Images')

# https://www.cs.cmu.edu/~rgs/alice-table.html

def clean_text(text):
    text = text.replace('`', '')\
            .replace('-\n', '')\
            .replace('\n\n', '&&***&&')\
            .replace('\n', '')\
            .replace('&&***&&', '\n\n')\
            .strip()
    return text

st.sidebar.image('https://docs.streamlit.io/logo.svg', width=100)
st.sidebar.header('Options')
text = st.sidebar.text_area('Paste Text Here', '''CHAPTER I

Down the Rabbit-Hole

Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?'

So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.

There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, `Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge. ''')
button1 = st.sidebar.button('Clean Text')

if button1:
    # st.write(text)
    # st.write(clean_text(text))

    col1, col2 = st.columns(2)
    col1_expander = col1.expander('Expand Original')
    col2_expander = col2.expander('Expand Cleaned')

    with col1_expander:
        st.header('Original Text')
        st.write(text)

    with col2_expander:
        st.header('Cleaned Text')        
        st.write(clean_text(text))


    # col1.header('Original Text')
    # col1.write(text)

    # col2.header('Cleaned Text')
    # col2.write(clean_text(text))

    # # version 1.12
    # with col1:
    #     st.header('Original Text')
    #     st.write(text)

    # with col2:
    #     st.header('Cleaned Text')
    #     st.write(clean_text(text))

## Lesson 2 Ends