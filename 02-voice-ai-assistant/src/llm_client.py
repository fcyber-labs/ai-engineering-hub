
from groq import Groq
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv(override=True)

#  LLM Client 
# Initialize clients with caching
@st.cache_resource
def init_clients(model_option, groq_api_key):
    """Initialize and cache API clients"""

    
    llm_text = ChatGroq(
        temperature=0.7,
        model=model_option,
        groq_api_key=groq_api_key
    )
    
    audio_client = Groq(api_key=groq_api_key)
    
    return llm_text, audio_client
