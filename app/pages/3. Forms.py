# Run this using:
# streamlit run "streamlit tutorial.py"

import streamlit as st
import spacy

# ## Lesson 3 Start  ##################################################

st.title('3. Forms')

# Forms are useful to prevent streamlit constantly updating with every selection. Forms let the user select items 
# first, then update after pressing a button or something. This is more computationally efficient.

nlp = spacy.load('en_core_web_lg')
# nlp = spacy.load('../en_core_web_lg')

def extract_entities(ent_pos_types, text):
    results = []

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_pos_types:
            results.append(f'{ent.text} [{ent.label_}]')

    for token in doc:
        if token.pos_ in ent_pos_types:
            results.append(f'{token.text} [{token.pos_}]')
    
    return results

form1 = st.sidebar.form(key='Options')

form1.header('Named Entity Recognition and Part of Speech')  # st.sidebar.header('Params')
ent_pos_types = form1.multiselect('Select the named entities or part of speech you want to extract', ['PERSON', 'ORG', 'GPE', 'NOUN', 'PROPN', 'VERB'])  # ent_types = st.sidebar.multiselect('Select the entities you want to extract', ['PERSON', 'ORG', 'GPE'])

# st.sidebar.button('Click Me')

form1.form_submit_button('Display')

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
Associate Professor, (Policy, Curriculum and Leadership)''', height=460)

hits = extract_entities(ent_pos_types, text)
st.write(hits)

## Lesson 3 Ends