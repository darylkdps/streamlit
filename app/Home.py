import streamlit as st

def main():
    st.title('Home Page - Test of Streamlit Functionality')
    st.text(st.secrets['test_token'])

if __name__ == '__main__':
    st.set_page_config(page_title="Daryl Test", page_icon="random", layout="wide", initial_sidebar_state="auto")
    main()

