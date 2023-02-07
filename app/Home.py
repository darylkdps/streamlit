import streamlit as st
import pandas as pd
import plotly.express as px
import spacy

st.set_page_config(
    page_title='Semantic Ruler',
    page_icon='random',
    layout='wide',
    initial_sidebar_state='auto'
    )

st.title('Semantic Ruler')

@st.cache(allow_output_mutation=True)
def load_model():
    spacy.require_cpu()
    return spacy.load('en_core_web_lg')
nlp = load_model()

default_title_word = 'leadership'
default_content_words = '''paper, pen, priority, decision, effort, mentor, stewardship, education, accountability, governance, leader, visualisation, cuisine, transform, chemistry, translate'''

title_word = st.text_input(
    label='Input Title Word:',
    value=default_title_word,
    )

content_words = st.text_input(
    label='Input content words separated by a comma:',
    value=default_content_words,
    )

title_word_cleaned = list(map(str.strip, title_word))
content_words_cleaned = list(map(str.strip, content_words.split(',')))

df = pd.DataFrame(data={'Title Word': [title_word] * len(content_words_cleaned), 'Content Word': content_words_cleaned})
df['Cosine Similarity'] = df.apply(lambda row: nlp.vocab[row['Title Word']].similarity(nlp.vocab[row['Content Word']]), axis=1).astype(float).round(3)
df = df.sort_values(by=['Cosine Similarity'])
# st.dataframe(df)

fig = px.bar(
    df,
    x='Cosine Similarity',
    y='Content Word',
    range_x=[0,1],
    text_auto='.3f',
    text='Cosine Similarity',
    template='plotly_dark',
    title='Cosine Similarity between Title Word <b>%s</b> and <i>content word</i>' % title_word.upper(),
    width=1000,
    height=1000
)

fig.update_traces(
    # marker_color='cyan'
)

fig.update_layout(
    title_x=0.5,
    title_font_size=18,
    xaxis_dtick=0.1,
    )

st.plotly_chart(
    fig,
    use_container_width=True,
    theme=None,
    )