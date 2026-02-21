
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv(override=True)

#  LLM Client 
# Initialize clients with caching
@st.cache_resource
def init_clients(groq_api_key):
    """Initialize and cache API clients"""

    
    llm = ChatGroq(
        temperature=0.7,
        model="openai/gpt-oss-120b",
        groq_api_key=groq_api_key
    )

    
    return llm
