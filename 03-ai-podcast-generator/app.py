


import streamlit as st


from datetime import datetime
import time



from src.nodes import scraper_rate_node, content_extractor_node, summarizer_node, podcast_script_writer_node, save_and_speak_node
from src.state import AgentState
from src.api_client import init_clients


# Streamlit part


# Streamlit Setup
start = time.time()


# initial sidebar state
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

    #  Header
    st.header("🎙️ AI Podcast News")
    st.caption("Turn top AI/news headlines into listenable episodes")


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








    #  Features Showcase
    st.divider()
    st.subheader("✨ Key Features")

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
        - **LangGraph**
        - **Groq** (fast LLM inference)
        - **gTTS** (text-to-speech)

        Created for quick AI-news podcast prototyping.
        Enjoy responsibly! 🚀
        """)

    #  Small footer note
    st.markdown(
        "<small style='color: gray;'>https://github.com/fcyber101/ai-engineering-hub</small>",
        unsafe_allow_html=True
    )






# Check API key    

# Check if key exists before calling

if st.session_state.api_key_valid and st.session_state.groq_api_key:
    llm = init_clients(st.session_state.groq_api_key)
else:
    st.error("👈 Please enter a valid GROQ API key")
    st.stop()


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

example_urls_2 = """https://www.bensbites.com
https://syncedreview.com
https://machinelearningmastery.com"""


# One key controls everything
if "urls" not in st.session_state:
    st.session_state.urls = ""

if st.button("📋 Load Example 1"): 
    st.session_state.urls = example_urls_1
    st.rerun()
if st.button("📋 Load Example 2"): 
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
        st.error("Please enter your Groq API Key")
        st.stop()

    
    urls_to_process = urls_input if urls_input.strip() else st.session_state.urls
    
    if not urls_to_process.strip():
        st.error("Please enter at least one URL")
        st.stop()
    

    
    # Parse URLs
    urls = []
    for line in urls_to_process.split('\n'):
        for url in line.split(','):
            url = url.strip()
            if url and url.startswith('http'):
                urls.append(url)
    
    if not urls:
        st.error("No valid URLs found")
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
    
    # Update progress function
    def update_progress(step, total_steps=8, message=""):
        progress = (step + 1) / total_steps
        progress_bar.progress(progress)
        status_text.text(f"Step {step + 1}/{total_steps}: {message}")

    try:
        # Step 1: Initialize
        update_progress(0, message="Initializing...")
        

        initial_state = AgentState(
            urls=urls,
            results=[], messages=[], top_20_articles=[], route="",
            full_articles=[], summarized_articles=[], summary_stats={},
            extraction_stats={}, podcast_script=None, podcast_metadata={},
            saved_files={}, human_feedback="proceed",  # Auto-proceed
            url_grade="yes", url_reasoning="Auto-approved for Streamlit",

        )
        
        # Step 2: Scrape and rate articles
        update_progress(1, message="Scraping/Rating articles...")
        log_output.text("🕸️ Scraping websites...")
        
        # Run scraper_rate_node directly
        scraped_state = scraper_rate_node(initial_state, llm)
        
        if "top_20_articles" in scraped_state:
            articles = scraped_state["top_20_articles"]
            log_output.text(f"✅ Found {len(articles)} top articles")
        
        update_progress(2, message="Extracting content...")
        log_output.text("📖 Extracting article content...")
        
        # Step 3: Extract content
        extracted_state = content_extractor_node(scraped_state)
        
        if "full_articles" in extracted_state:
            articles = extracted_state["full_articles"]
            successful = len([a for a in articles if a.get("full_text")])
            log_output.text(f"✅ Extracted {successful} articles successfully")
        
        update_progress(3, message="Creating summaries...")
        log_output.text("📝 Summarizing articles...")
        
        # Step 4: Summarize - API ONLY
        summarized_state = summarizer_node(extracted_state, llm) 

        st.caption("Using API-based summarization (LLM)")
        
        if "summary_stats" in summarized_state:
            stats = summarized_state["summary_stats"]
            log_output.text(f"✅ Created {stats.get('successfully_summarized', 0)} summaries")
        
        update_progress(4, message="Writing podcast script...")
        log_output.text("🎙️ Writing podcast script...")
        
        # Step 5: Create podcast script
        script_state = podcast_script_writer_node(summarized_state, llm)
        
        if "podcast_script" in script_state:
            script = script_state["podcast_script"]
            metadata = script_state.get("podcast_metadata", {})
            log_output.text(f"✅ Script created: {metadata.get('total_words', 0)} words")
        
        update_progress(5, message="Generating audio...")
        log_output.text("🔊 Converting text to speech...")
        
        # Step 6: Generate audio
        final_state = save_and_speak_node(script_state)
        
        update_progress(6, message="Finalizing...")
        
        # Display results
        progress_bar.empty()
        status_text.empty()
        
        # SUCCESS MESSAGE
        st.success("✅ Podcast generated successfully!")
        
        # Display podcast script
        with st.expander("📄 Podcast Script", expanded=True):
            script = final_state.get("podcast_script", "")
            if script:
                st.text_area("Script", script, height=300)
            else:
                st.warning("No script generated")

        # Streamlit audio display 

        # Get buffer from state
        audio_buffer = final_state.get("audio_buffer") 

        if audio_buffer:
            st.subheader("Podcast Audio 🎧")
            
            # Center player
            col1, col2, col3 = st.columns([1, 4, 1])
            with col2:
                st.audio(audio_buffer, format="audio/mp3", autoplay=True) 
            
            # Download

            # Reset buffer position
            audio_buffer.seek(0) 
            st.download_button(
                "Download MP3",
                audio_buffer,
                file_name=final_state.get("saved_files", {}).get("mp3_file", "podcast.mp3"),
                mime="audio/mp3"
            )

            st.download_button(
                "📥 Download Script (TXT)",
                script,
                file_name=f"podcast_script_{st.session_state.current_date}.txt",
                mime="text/plain"
            )
        else:
            st.warning("Audio generation failed or file not found.")

        
        # Display stats
        end = time.time()
        duration = (end-start)/60
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if "top_20_articles" in scraped_state:
                st.metric("Best Articles Found", len(scraped_state["top_20_articles"]))
        
        with col2:
            if "summary_stats" in summarized_state:
                stats = summarized_state["summary_stats"]
                st.metric("Good Summaries", stats.get("successfully_summarized", 0))
        
        with col3:
            if "podcast_metadata" in script_state:
                metadata = script_state["podcast_metadata"]
                st.metric("Process's Duration", f"{duration:.2f} minutes")
        
        # Show successfully summarized articles
        st.subheader("📝 Summarized Articles")

        # Get the summarized articles from state
        if "summarized_articles" in final_state:
            # Filter for successful summaries
            successful_articles = [
                article for article in final_state["summarized_articles"]
                if article.get("summary_status") == "success" 
            ]
            
            # Sort by score if available
            successful_articles.sort(key=lambda x: x.get("llm_score", x.get("rate", 0)), reverse=True)
            
            if successful_articles:
                st.success(f"✅ {len(successful_articles)} articles successfully summarized")
                
                # Show top 5 successful articles
                for i, article in enumerate(successful_articles[:5], 1):
                    title = article.get("title", "Untitled")
                    score = article.get("llm_score", article.get("rate", 0))  
                    url = article.get("url", "")
                    summary = article.get("summary", "")
                    quality = article.get("quality_check", "Unknown")
                    
                    with st.expander(f"{i}. {title[:60]}..."):
                        # Score and quality
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Rating:** {score}/100")
                            st.progress(score / 100)
                        with col2:
                            st.markdown(f"**Quality:** {quality}")
                        
                        # URL
                        st.markdown(f"**URL:** {url[:80]}...")
                        
                        # Show the summary if available
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