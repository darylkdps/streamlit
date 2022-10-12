# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st
import spacy

## Lesson 4 Start  ##################################################

st.title('4. Caching Models and Data')

@st.cache(allow_output_mutation=True)
def load_model(model_name):
    return spacy.load(model_name)

nlp = load_model('en_core_web_lg')

def extract_entities(ent_pos_types, text):
    results = []

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_pos_types:
            results.append( f'{ent.text} [{ent.start}:{ent.end}) [{ent.label_}]')

    for token in doc:
        if token.pos_ in ent_pos_types:
            results.append(f'{token.text} [{token.i}] [{token.pos_}]')
    
    return results

st.sidebar.header('Named Entity Recognition and Part of Speech')
ent_pos_types = st.sidebar.multiselect('Select the named entities or part of speech you want to extract', ['PERSON', 'ORG', 'GPE', 'NOUN', 'PROPN', 'VERB'])

text = st.text_area('Sample Text', '''The Strategic Planning and Academic Quality (SPAQ) office was established on 15 March 2014 after a re-organisation to incorporate the key functions of strategic planning and academic quality management into a single office. It aims to tap on the synergies and linkages between strategic planning and evidence-informed academic quality enhancement efforts to aid institute-wide planning, decision-making and quality assurance. Please click here to view SPAQ’s Framework and click here to view SPAQ's function.

Each of the functions under SPAQ is led by a head of department that reports directly to the Dean, Academic and Strategic Development. The Strategic Planning Unit is headed by Ms Wong Su Ling and the Academic Quality Unit is headed by Associate Professor David Ng Foo Seong.

The Strategic Planning unit assists the NIE leadership in overseeing the formulation, implementation and communication of the Institute’s medium term strategic plan. The current NIE Strategic Vision 2022: "A Future-Ready National Institute of Education" outlines NIE's key strategic direction and institute-level goals for the next few years. 

The unit is also the Secretariat for the meetings of the NIE Council and its Executive Committee, the Director’s Strategic Review and Development Meeting (DSM), the MOE-NIE Coordination Committee (MNCC) and the MOE-NIE Working Group (MNWG). 

The Academic Quality unit takes the lead in helping to promote a culture of continuous self-improvement and the adoption of best practices for NIE academic programmes. Through the gathering of evidence-based feedback from various stakeholders, trend analysis and academic reviews, SPAQ provides deep insight and analysis to aid programmatic and pedagogical enhancements.
''', height=400)

hits = extract_entities(ent_pos_types, text)
st.write(hits)

doc = nlp(text)
st.markdown(spacy.displacy.render(doc, style='ent', options={'ents': ['PERSON', 'ORG', 'GPE']}, jupyter=False), unsafe_allow_html=True)

st.markdown(spacy.displacy.render(list(doc.sents)[1].as_doc(), style='dep', options={'add_lemma': True, 'compact': False}, jupyter=False), unsafe_allow_html=True)


## Lesson 4 Ends