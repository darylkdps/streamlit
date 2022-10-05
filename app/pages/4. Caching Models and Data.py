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

text = st.text_area('Sample Text', '''The National Institute of Education (NIE), Singapore, is Singapore’s national teacher education institute and we are proud to be an integral part of the nation’s education service. We play a key role in the preparation of teachers and in the provision of teacher professional and school leadership development programmes. 
 
Our university-based teacher education programmes leverage the strong partnerships that NIE has with the Ministry of Education and Singapore schools to develop teachers who are grounded in theory and strong in practice. As an institute within a world-class research university, NIE also offers rigorous graduate education in the form of masters and doctoral programmes for local and international students. 
 
NIE faculty are actively involved in research in their respective academic disciplines. Our education research strengthens the research-practice nexus continually, and advances theory and policy thinking. NIE also supports our nation’s life-long learning endeavours through courses in relevant professional and life skills. 
  
I thank you for your interest in NIE and warmly welcome you to find out more about our people and our work. 
 
Professor Christine Goh
----------
Extracted from NIE's web page by Daryl Ku.

His boss is:
Associate Professor David Ng Foo Seong
Associate Dean (Academic Quality, Office of Academic & Strategic Development)
Associate Professor, (Policy, Curriculum and Leadership)

His grandboss is:
Professor Chang Chew Hung
Dean, Academic and Strategic Development
Professor, Humanities & Social Studies Education 
''', height=500)

hits = extract_entities(ent_pos_types, text)
st.write(hits)

doc = nlp(text)
st.markdown(spacy.displacy.render(doc, style='ent', options={'ents': ['PERSON', 'ORG', 'GPE']}, jupyter=False), unsafe_allow_html=True)

st.markdown(spacy.displacy.render(list(doc.sents)[3].as_doc(), style='dep', options={'add_lemma': True, 'compact': False}, jupyter=False), unsafe_allow_html=True)


## Lesson 4 Ends