import streamlit as st

import io

from langchain_core.messages import HumanMessage, SystemMessage


from src.audio_processor import generate_audio
from src.llm_client import init_clients
from config import MODEL_OPTIONS, LANGUAGES


#  Main interface 


#  INITIALIZE SESSION STATE 
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "processing" not in st.session_state:
    st.session_state.processing = False


#  Configure page 
# Configure page
st.set_page_config(
    page_title="Voice AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main interface
st.title("🤖 Voice AI Assistant")
st.caption("Record your voice, get AI responses with speech synthesis")


#  Sidebar 
# Sidebar configuration
with st.sidebar:
    st.header("Configuration")
    
    # API Key
    api_key = st.text_input(
        "GROQ API Key 🔑", 
        type="password",
        value=st.session_state.get("api_key", "")
    )
    
    # Validate API key
    if api_key:
        st.session_state.api_key = api_key
        if api_key.startswith("gsk_"):
            st.session_state.api_key_valid = True
            st.success("✅ API key ready", icon="🔑")
        else:
            st.session_state.api_key_valid = False
            st.warning("⚠️ API key should start with 'gsk_'")
    else:
        st.session_state.api_key_valid = False
        st.info("👆 Enter your GROQ API key to begin")
    
    # Model selection
    model_option = st.selectbox(
        "Select LLM Model",
        options=list(MODEL_OPTIONS.keys())
    )
    selected_model = MODEL_OPTIONS[model_option]
    # Voice settings
    voice_lang = st.selectbox("Voice Language", options=list(LANGUAGES))
    slow_speech = st.checkbox("Slow Speech", value=False)
    
    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.conversation = []
        st.rerun()
    
    # Display stats
    st.divider()
    st.caption(f"Conversation turns: {len(st.session_state.conversation)}")



try:
    llm_text, audio_client = init_clients(selected_model, groq_api_key)
except Exception as e:
    st.error(f"Failed to initialize clients: {e}")
    st.stop()


#  Conversation History 
# Conversation display 



    
if st.session_state.conversation:
    st.divider()
    st.subheader("Conversation History")
    
    for i, (user_msg, ai_msg) in enumerate(st.session_state.conversation):
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.text("You:")  
            with col2:
                st.write(user_msg) 
            
            with col1:
                st.text("AI:")  
            with col2:
                st.write(ai_msg) 
        
        if i < len(st.session_state.conversation) - 1:
            st.divider()

# Audio input section
st.divider()
st.subheader("Voice Input")

audio_record = st.audio_input("Press to record your message", key="audio_input")

if audio_record:
    with st.spinner("Processing your voice..."):
        try:
            # Process audio
            audio_bytes = audio_record.read()
            audio_file = io.BytesIO(audio_bytes)
            audio_file.name = "query.mp3"
            
            # Transcribe
            progress_bar = st.progress(0, text="Transcribing audio...")
            transcript = audio_client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3-turbo",
                language="en"
            )
            progress_bar.progress(100, text="Transcription complete!")
            
            text_query = transcript.text
            
            # Display transcription
            with st.expander("Transcription Details", expanded=False):
                st.write(text_query)
                st.caption(f"Character count: {len(text_query)}")
            
            # Generate AI response
            progress_bar = st.progress(0, text="Generating AI response...")
            

            system_prompt = SystemMessage(
                content=(
                    f"You are a helpful AI assistant. Provide a clear, concise answer in {voice_lang} only. "
                    f"Respond in 1-3 sentences. Be constructive and helpful."
                )
            )
            human_message = HumanMessage(content=text_query)
            
            messages = [system_prompt, human_message]
            response = llm_text.invoke(messages)
            answer = response.content
            
            progress_bar.progress(100, text="Response generated!")
            
            # Add to conversation history
            st.session_state.conversation.append((text_query, answer))
            
            # Display response
            st.success("Response Ready!")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader("AI Response")
                st.write(answer)  
            
            # Text-to-speech with multilingual support
            with st.spinner("Generating speech..."):

                audio_bytes = generate_audio(answer, voice_lang, slow_speech)

                
                # Audio player with controls
                st.subheader("Audio Response")
                
                audio_col1, audio_col2, audio_col3 = st.columns([1, 2, 1])
                with audio_col2:
                    st.audio(
                        audio_bytes, 
                        format="audio/mp3",
                        start_time=0,
                        autoplay=True
                    )
                
                # Download button
                audio_bytes.seek(0)
                st.download_button(
                    label="Download Audio",
                    data=audio_bytes,
                    file_name="ai_response.mp3",
                    mime="audio/mp3"
                )
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please try again or check your API keys.")


#  FOOTER 
st.divider()
st.caption("Powered by Groq API, Whisper, and gTTS")

# Instructions
with st.expander("How to use"):
    st.write("1. Record: Click the microphone button and speak")
    st.write("2. Transcription: Your speech is converted to text")
    st.write("3. AI Processing: The AI generates a response")
    st.write("4. Audio Output: Listen to the AI's spoken response")
    st.write("5. History: View past conversations in the sidebar")

# Performance tips
with st.expander("Performance Tips"):
    st.write("- Clear conversation periodically to free memory")
    st.write("- Use shorter recordings for faster processing")
    st.write("- Check your Groq API quota in the dashboard")
    st.write("- For better voice quality, consider edge-tts instead of gTTS")