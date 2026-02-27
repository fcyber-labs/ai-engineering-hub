

from src.config import top50_urls

import streamlit as st
import os
from datetime import datetime

import time




from src.nodes import scraper_rate_node, content_extractor_node, summarizer_node, podcast_script_writer_node, save_and_speak_node, text_to_mp3
from src.state import AgentState
from src.api_client import init_clients

from src.workflow import graph_app



if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = os.getenv("GROQ_API_KEY", "")

model_option = "openai/gpt-oss-120b"
# Streamlit Setup
start = time.time()


st.set_page_config(
    page_title="🎧 AI Podcast News",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",     
)
st.title("🎧 AI News Podcast - AI DAILY DIGEST")

if "current_date" not in st.session_state:
    st.session_state.current_date = datetime.now().strftime("%Y_%m_%d")



# Sidebar
with st.sidebar:

    # Header / Branding
    st.header("🎙️ AI Podcast News")
    st.caption("Turn top AI/news headlines into listenable episodes")

    # API Key input

    # Import QROQ API key

      
    # API Key
    groq_api_key = st.sidebar.text_input("GROQ API Key 🔑 ", type="password")

    # Model selection
    MODEL = "openai/gpt-oss-120b"

    # Validate API key
    if groq_api_key:
        st.session_state.groq_api_key = groq_api_key
        if groq_api_key.startswith("gsk_"):
            st.session_state.api_key_valid = True
            st.success("✅ API key ready", icon="🔑")
        else:
            st.session_state.api_key_valid = False
            st.warning("⚠️ API key should start with 'gsk_'")
            groq_api_key = None
    else:
        st.session_state.api_key_valid = False
        st.info("👆 Enter your GROQ API key to begin")





    SUMMARY_OPTIONS = {
        "API summary method": "api",
        "BART Large CNN": "bart"
    }
    # Features Showcase
    st.divider()
    st.subheader("✨ Key Features")
    summary_method = st.selectbox(
        "Select LLM Model",
        options=list(SUMMARY_OPTIONS.keys()))


    summary_method = SUMMARY_OPTIONS[summary_method]

    features = [
        ("🧠 LLM-powered", "Intelligent script writing & voice synthesis"),
        ("📥 Download", "Save script (.txt) + audio (.mp3)"),
        ("🔄 LangGraph", "Structured, reliable multi-step workflow"),
        ("🏆 Headline Rating", "Smart scoring of most promising news titles"),
        ("📊 Top-10 Summary", "Condensed insights with LLM"),
        ("▶️ Instant Listen", "Play generated podcast right in browser")
    ]

    for icon, desc in features:
        st.markdown(f"{icon} **{desc.split(' ', 1)[0]}** — {desc.split(' ', 1)[1]}")

    #  Quick Actions 
    st.divider()
    st.subheader("Controls")

    if st.button("🔄 Reset Session", use_container_width=True, type="secondary"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # Info
    with st.expander("About & Tech Stack", expanded=False):
        st.markdown("""
        Built with:
        - **Streamlit** (frontend)
        - **LangGraph** (workflow orchestration)
        - **Groq** (fast LLM inference)
        - **gTTS** (text-to-speech)

        Created for quick AI-news podcast prototyping.
        Enjoy responsibly! 🚀
        """)

    #  Footer note
    st.markdown(
        "<small style='color: gray;'>https://github.com/fcyber-labs/</small>", 
        unsafe_allow_html=True
    )






# Main content
st.markdown("Enter news URLs to generate an AI podcast automatically")

# URL Input
urls_input = st.text_area(
    "Enter URLs (one per line or comma-separated):",
    placeholder="https://techcrunch.com/tag/artificial-intelligence/",
    height=100
)

# Example URLs
example_urls_1 = """https://www.marktechpost.com
https://www.kdnuggets.com
https://theresanaiforthat.com"""

example_urls_2 = """https://techcrunch.com/tag/artificial-intelligence/

"""
# https://syncedreview.com
# https://machinelearningmastery.com

example_urls_3 = """https://news.ycombinator.com/
https://news.ycombinator.com/?p=2
https://news.ycombinator.com/?p=3
https://news.ycombinator.com/?p=4
"""
example_urls_4 = '\n'.join(top50_urls)

# One key controls everything
if "urls" not in st.session_state:
    st.session_state.urls = ""

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔥 TOP BEST 50 AI news websites"):
        st.session_state.urls = example_urls_4
        st.rerun()

with col2:
    if st.button("🤩 Best of Hacker News"):
        st.session_state.urls = example_urls_3
        st.rerun()

with col3:
    if st.button("🤠 Load 3 URLs Example"):
        st.session_state.urls = example_urls_1
        st.rerun()

with col4:
    if st.button("👍 Load 1 URL Example"):
        st.session_state.urls = example_urls_2
        st.rerun()


st.text_area(
    "URLs",
    value=st.session_state.urls,
    height=120, disabled=True
)

# Generate Button
if st.button("😎 Generate Podcast", type="primary"):
    if not groq_api_key:
        st.warning("Please enter your Groq API Key")
        st.stop()


    if st.session_state.api_key_valid and st.session_state.groq_api_key:
        llm = init_clients(st.session_state.groq_api_key)
    else:
        st.error("👈 Please enter a valid GROQ API key")
        st.stop()
    

    
    urls_to_process = urls_input if urls_input.strip() else st.session_state.urls
    
    if not urls_to_process.strip():
        st.warning("Please enter at least one URL")
        st.stop()

    

    # Parse URLs
    urls = []
    for line in urls_to_process.split('\n'):
        for url in line.split(','):
            url = url.strip()
            if url and url.startswith('http'):
                urls.append(url)
    
    if not urls:
        st.warning("No valid URLs found")
        st.stop()
    
    # Display progress
    st.info(f"Processing {len(urls)} URLs...")
    
    # Create progress container
    progress_container = st.container()
    log_container = st.container()
    
    with progress_container:
        progress_bar = st.progress(0)
        status_text = st.empty()
    
    with log_container:
        log_output = st.empty()
        state_display = st.empty()
    
    # Update progress
    def update_progress(step, message=""): 
        total_steps = 6  

        # total_steps = int(total_steps)          

        progress = step / int(total_steps)       

        progress = step / float(total_steps)    

        progress_bar.progress(progress)
        status_text.text(f"{message} ({step}/{total_steps})")
    
    try:
        # Initialize
        update_progress(1, message="Initializing...")
        
        # Import your functions
        from langgraph.graph import StateGraph, END
        



        # Create initial state
        initial_state = AgentState(
            urls=urls,
            llm=llm, 
            results=[], messages=[], top_20_articles=[], route="",
            full_articles=[], summarized_articles=[], summary_stats={},
            extraction_stats={}, podcast_script=None, podcast_metadata={},
            saved_files={}, human_feedback="proceed",
            url_grade="yes", url_reasoning="Auto-approved for Streamlit",
            summary_method=summary_method  
        )
        
        # Run the compiled graph and stream updates

        log_output.text("🚀 Running LangGraph workflow...")

        final_state = None
        script_text = None



        for step_idx, step_output in enumerate(graph_app.stream(initial_state)):
            for node_name, node_update in step_output.items():
                if node_name == "__start__":
                    continue

                # Progress messages – use node_update 
                if node_name == "scraper_rate_node":
                    update_progress(2, "Scraping/Rating articles...")
                    if "top_20_articles" in node_update:
                        # log_output.text(f"🕸️ Found {len(node_update['top_20_articles'])} Best AI articles")
                        state_display.info(f"📊 Extracting content for {len(node_update['top_20_articles'])} top articles")

                elif node_name == "content_extractor_node":
                    update_progress(3, "Extracting content...")
                    if "extraction_stats" in node_update:

                        stats = node_update["extraction_stats"]
                        state_display.info(f"✅ Extracted {stats.get('successful', 0)} articles")

                elif node_name in ["summarizer_node", "summarize_bart_node"]:
                    update_progress(4, "Creating summaries...")
                    if "summary_stats" in node_update:

                        stats = node_update["summary_stats"]
                        state_display.info(f"✅ {stats.get('successfully_summarized', 0)} summaries")

                elif node_name == "podcast_script_writer_node":
                    update_progress(5, "Writing podcast script...")

                    if "podcast_script" in node_update:
                        script_text = node_update["podcast_script"]          
                        st.session_state.last_podcast_script = script_text     
                    if "podcast_metadata" in node_update:
                        meta = node_update["podcast_metadata"]
                        state_display.info(f"Script: {meta.get('total_words', 0)} words")

                elif node_name == "save_and_speak_node":
                    update_progress(6, "Saving files...")
                    if "saved_files" in node_update:
                        files = node_update["saved_files"]
                        state_display.success(f"Files saved: {files.get('mp3_file', '—')}")

                final_state = {** (final_state or {}), **node_update}  


        # Generate audio ONLY after graph is done


        audio_buffer = None

        if script_text or st.session_state.get("last_podcast_script"):
            script_to_use = script_text or st.session_state.get("last_podcast_script")
            
            with st.spinner("🎙️ Generating audio (gTTS)…"):
                try:
                    mp3_filename, audio_buffer = text_to_mp3(
                        script_to_use,
                        language="en",
                        filename_prefix="ai_podcast"
                    )
                    st.session_state.audio_buffer = audio_buffer
                    st.session_state.audio_filename = mp3_filename
                    st.success(f"Audio created ({len(audio_buffer.getvalue()) // 1024:,} KB)")
                except Exception as exc:
                    st.error(f"Audio generation failed: {exc}")
                    st.session_state.audio_buffer = None


        #  Display everything


        progress_bar.empty()
        status_text.empty()
        state_display.empty()

        st.success("✅ Podcast ready!")

        if final_state:
            # Script
            with st.expander("📄 Podcast Script", expanded=True):
                script = script_text or final_state.get("podcast_script", "")
                st.text_area("Script", script, height=300)

            # Audio
            audio_buffer = st.session_state.get("audio_buffer")

            if audio_buffer and len(audio_buffer.getvalue()) > 2000:
                audio_buffer.seek(0)
                st.subheader("Podcast Audio 🎧")
                
                col1, col2, col3 = st.columns([1, 4, 1])
                with col2:
                    st.audio(audio_buffer, format="audio/mp3", autoplay=True)

                audio_buffer.seek(0)
                st.download_button(
                    "Download MP3",
                    audio_buffer,
                    file_name=st.session_state.get("audio_filename", "podcast.mp3"),
                    mime="audio/mp3"
                )

                st.download_button(
                    "Download Script",
                    script,
                    file_name=f"podcast_script_{datetime.now().strftime('%Y-%m-%d')}.txt",
                    mime="text/plain"
                )
            else:
                st.warning("No valid audio was generated.")




            
            # Display stats
            end = time.time()
            duration = (end-start)/60
            col1, col2, col3 = st.columns(3)
            
            with col1:
                top_articles = final_state.get("top_20_articles", [])
                st.metric("Articles Found", len(top_articles))
            
            with col2:
                summary_stats = final_state.get("summary_stats", {})
                st.metric("Good Summaries", summary_stats.get("successfully_summarized", 0))
            
            with col3:
                metadata = final_state.get("podcast_metadata", {})
                st.metric("Process Duration", f"{duration:.2f} minutes")
            
            # Show successfully summarized articles 
            method_display = "API (LLM)" if final_state.get("summary_method") == "api" else "BART Large (Local)"
            st.subheader(f"📝 Summarized Articles with **{method_display} method**")
            
            if "summarized_articles" in final_state:
                successful_articles = [
                    article for article in final_state["summarized_articles"]
                    if article.get("summary_status") == "success"
                ]
                
                successful_articles.sort(
                    key=lambda x: x.get("llm_score", x.get("rate", 0)), 
                    reverse=True
                )
                
                if successful_articles:
                    st.success(f"✅ {len(successful_articles)} articles successfully summarized")
                    
                    for i, article in enumerate(successful_articles[:5], 1):
                        title = article.get("title", "Untitled")
                        score = article.get("llm_score", article.get("rate", 0))
                        url = article.get("url", "")
                        summary = article.get("summary", "")
                        quality = article.get("quality_check", "Unknown")
                        
                        with st.expander(f"{i}. {title[:60]}..."):
                            col1, col2 = st.columns(2)
                            with col1:
                                st.markdown(f"**Rating:** {score}/100")
                                st.progress(score / 100)
                            with col2:
                                st.markdown(f"**Quality:** {quality}")
                            
                            st.markdown(f"**URL:** {url[:80]}...")
                            
                            if summary:
                                st.markdown("**Summary:**")
                                st.write(summary[:200] + "..." if len(summary) > 200 else summary)
                else:
                    st.warning("No articles were successfully summarized.")
            else:
                st.info("Waiting for summarization...")
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        import traceback
        st.code(traceback.format_exc())