import streamlit as st
import nltk
nltk.download('punkt')

st.set_page_config(
    page_title="MiN_FullstackGPT",
    page_icon="⭐️",
)

with st.sidebar:
    st.title("**Sidebar title")
    st.text_input("**Question?")

st.markdown(
    """
    # Hello!
    
    Welcome to my FullstackGPT Portfolio!
    
    Here are the apps I made:
    
    - 🍄 [DocumentGPT](/DocumentGPT)
    - [ ] [PrivateGPT](/PrivateGPT)
    - [ ] [QuizGPT](/QuizGPT)
    - [ ] [SiteGPT](/SiteGPT)
    - [ ] [MeetingGPT](/MeetingGPT)
    - [ ] [InvestorGPT](/InvestorGPT)
    """
)
