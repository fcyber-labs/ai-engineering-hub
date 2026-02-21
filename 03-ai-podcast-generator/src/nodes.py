

import cloudscraper
import requests.compat
import time

from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup
import re


from io import BytesIO
import html
from typing import List, Dict, Any
from typing_extensions import TypedDict, Annotated


from .api_client import init_clients


from .state import AgentState


def scrape_sites(url: str) -> List[dict]:
    """Scrape blocked sites and save results as dict with title and link"""
    save_date = time.strftime("%Y_%m_%d")
    results = []  # This will store our dicts
    
    try:
        scraper = cloudscraper.create_scraper()
        print(f"🚀 Bypassing protection for: {url}")
        response = scraper.get(url, timeout=15)
        
        if response.status_code == 200:
            import re
            links = re.findall(r'<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>', response.text)
            print(f"✅ Success! Found {len(links)} total links")
            
            for href, text in links:
                text = text.strip()
                
                # Filter criteria
                if (20 < len(text) < 200 and
                    not text.lower().startswith(('click', 'read more', 'here', 'login', 'sign', 'cookie')) and
                    not text.isdigit() and
                    any(char.isalpha() for char in text)):
                    
                    text = html.unescape(text) 



                    # Make URL absolute
                    if href:
                        if href.startswith('/'):
                            href = requests.compat.urljoin(url, href)
                        elif href.startswith('#'):
                            continue
                        elif not href.startswith(('http://', 'https://')):
                            href = requests.compat.urljoin(url, href)
                    
                    # Append to results
                    results.append({
                        "date": save_date,
                        'title': text,
                        'link': href,
                        'source': url
                    })
            
            print(f"📊 Found {len(results)} meaningful headlines")
            return results
            
        else:
            print(f"❌ Still blocked: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return []










def smart_rate_titles(articles: List[dict], llm) -> List[dict]:
    """Use LLM with structured output to rate titles"""

    
    rated_articles = []
    
    # Rate each article
    for i, article in enumerate(articles[:1000]):  
        prompt = f"""You are an expert AI-news curator. Rate how central this headline is to **current artificial intelligence and machine learning news** on a 0–100 scale.

        Title: {article['title']}

        Rules:
        - 95–100: core topic is LLMs, foundation models, AI research, new releases, major companies (OpenAI, Anthropic, DeepMind, xAI, Meta AI, etc.), breakthroughs, safety/alignment/regulation
        - 70–94: clearly AI-related but secondary (funding, applications, criticism, hardware for AI)
        - 40–69: vague / tangential / hype / old news
        - <40: unrelated or only keyword match

        Output format: only the integer score, no explanation, no other text."""
        
        try:
            response = llm.invoke(prompt)
            # Extract the first number from the response
            import re
            match = re.search(r'(\d{1,3})', response.content)
            score = int(match.group(1)) if match else 0
            
            article['llm_score'] = score
            rated_articles.append(article) 
            print(f"  ✅ Rated: {score}/100")
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            article['llm_score'] = 0
            rated_articles.append(article) 
    
    # 🎯 SORT AND **RETURN**
    rated_articles.sort(key=lambda x: x['llm_score'], reverse=True)
    return rated_articles[:20]













def scraper_rate_node(state: AgentState, llm) -> AgentState:
    """Fixed version - removes duplicate URLs before rating"""
    
    urls_to_scrape = state.get("urls", [])
    
    all_articles = []
    for url in urls_to_scrape:
        articles = scrape_sites(url)
        if articles:
            all_articles.extend(articles)

#            # Save to JSON (optional)
#            with open('scraped_results.json', 'a', encoding='utf-8') as f:
#                # Save each article individually
#                for article in articles:
#                    json.dump(article, f, ensure_ascii=False)
#                    f.write('\n')  # Newline after each article
#            print(f"💾 Saved {len(articles)} articles from {url}")
    
    if not all_articles:
        return {
            **state,
            "results": [],
            "messages": ["No articles found"],
            "route": "content_extractor_node"
        }
    
    # REMOVE DUPLICATES BEFORE RATING
    unique_articles = {}
    for article in all_articles:
        url = article.get('link')
        if url and url not in unique_articles:
            unique_articles[url] = article



    
    unique_list = list(unique_articles.values())
    print(f"📊 Found {len(all_articles)} articles, {len(unique_list)} unique")
    
    # Rate unique articles
    top_articles = smart_rate_titles(articles=unique_list, llm=llm)
    
    # Format - ensure no duplicates
    output = []
    seen_urls = set()
    
    for article in top_articles[:10]:  # top articles !!!
        url = article.get('link')
        if url and url not in seen_urls:
            seen_urls.add(url)
            output.append({
                "rate": article.get('llm_score', 0),
                "url": url,
                "title": article['title']
            })
    
    print(f"🎯 Selected {len(output)} unique top articles")
    
    return {
        **state,
        "top_20_articles": output,
        "results": all_articles,
        "route": "content_extractor_node",
        "messages": [f"Found {len(output)} unique top articles"]
    }






def extract_article_content(url: str) -> Dict[str, Any]:
    """Extract content ONLY, no title needed!"""
    
    try:
        scraper = cloudscraper.create_scraper()
        scraper.headers.update({'User-789': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36'})
        response = scraper.get(url, timeout=25)
        
        if response.status_code != 200:
            return {"success": False, "error": f"HTTP {response.status_code}"}
        
        soup = BeautifulSoup(response.text, 'html.parser')
        

        
        # Remove unwanted elements
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 
                        'iframe', 'noscript', 'form', 'button']):
            tag.decompose()
        
        #  Try Substack-specific selectors first
        substack_selectors = [
            'article',
            '.post', '.post-content', '.article-content',
            '.published-content', '.body', '.content',
            '[data-testid="post-content"]',  
            'div[class*="post"]', 'div[class*="article"]',
            'main', 'main div', 'main article'
        ]
        
        content_text = ""
        best_selector = ""
        
        for selector in substack_selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text(separator='\n', strip=True)
                text = re.sub(r'\n\s*\n+', '\n\n', text)
                
                # Check for real article content
                if (len(text) > 800 and  # Substantial
                    len(text.split('\n')) > 10 and  
                    not any(word in text.lower() for word in ['subscribe', 'home', 'sign in', 'notes']) and
                    sum(1 for c in text if c.isalpha()) > 500): 
                    
                    if len(text) > len(content_text):
                        content_text = text
                        best_selector = selector
        
        # Fallback: Get all paragraphs and filter
        if not content_text:
            paragraphs = soup.find_all(['p', 'div'])
            good_paragraphs = []
            
            for p in paragraphs:
                text = p.get_text(strip=True)
                # Filter: meaningful paragraphs only
                if (len(text) > 150 and
                    sum(1 for c in text if c.isalpha()) > 100 and  # Enough letters
                    not any(word in text.lower() for word in ['subscribe', 'home', 'menu'])):
                    
                    # Check parent isn't navigation
                    parent = p.parent
                    parent_class = ' '.join(parent.get('class', [])) if parent else ''
                    if 'nav' not in parent_class.lower() and 'menu' not in parent_class.lower():
                        good_paragraphs.append(text)
            
            if good_paragraphs:
                content_text = '\n\n'.join(good_paragraphs)
                best_selector = "paragraphs_filtered"
        
        if content_text and len(content_text) > 500:
            return {
                "success": True,

                "full_text": content_text[:20000],
                "char_count": len(content_text),
                "method": f"article_page: {best_selector}",
                "url": url  # Keep original URL for reference
            }
        
        return {"success": False, "error": "No article content found"}
        
        
    except Exception as e:
        return {"success": False, "error": str(e)}



def content_extractor_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Node that extracts full content - HANDLES DUPLICATES"""
    
    top_articles = state.get("top_20_articles", [])
    
    if not top_articles:
        return state
    
    print(f"📖 Extracting content for {len(top_articles)} articles...")
    
    full_articles_data = []
    success_count = 0
    processed_urls = set() 
    
    for i, article in enumerate(top_articles, 1):
        url = article["url"]
        
        # SKIP DUPLICATE URLS
        if url in processed_urls:
            print(f"  [{i}/{len(top_articles)}] ⚠️ Skipping duplicate: {url[:50]}...")
            continue
        processed_urls.add(url)
        
        article_title = article.get("title", "Untitled")
        print(f"  [{i}/{len(top_articles)}] Extracting: {article_title[:60]}...")
        
        # EXTRACT CONTENT
        result = extract_article_content(url)
        
        if result.get("success"):
            full_article = {
                "llm_score": article.get("rate", 0),
                "title": article_title,
                "url": url,
                "full_text": result["full_text"][:10000],
                "char_count": result["char_count"],
                "extraction_method": result["method"],
                "extraction_time": time.strftime("%H:%M:%S"),
                "source_url": url
            }
            full_articles_data.append(full_article)
            success_count += 1
            print(f"    ✅ Success ({result['char_count']} chars)")
        else:
            print(f"    ❌ Failed: {result.get('error', 'Unknown error')}")
            full_articles_data.append({
                "llm_score": article.get("rate", 0),
                "title": article_title,
                "url": url,
                "full_text": "",
                "error": result.get("error", "Extraction failed"),
                "char_count": 0
            })
        
        time.sleep(1)
    
    print(f"📊 Extraction complete: {success_count}/{len(processed_urls)} successful (after removing duplicates)")
    
    return {
        **state,
        "full_articles": full_articles_data,
        "extraction_stats": {
            "total_original": len(top_articles),
            "unique_urls": len(processed_urls),
            "successful": success_count,
            "success_rate": f"{(success_count/len(processed_urls))*100:.1f}%"
        },
        "messages": state.get("messages", []) + [
            f"✅ Extracted content: {success_count}/{len(processed_urls)} unique articles"
        ]
    }










def summarize_article_checker(full_articles: List[Dict[str, Any]], llm) -> List[Dict[str, Any]]:
    """LLM agent: Check content quality and create 200-word summaries - FIXED"""
    
    if not full_articles:
        return []
    
    print(f"🤖 Summarizing {len(full_articles)} articles with LLM...")
    
    summarized_articles = []
    
    for i, article in enumerate(full_articles, 1):
        print(f"  [{i}/{len(full_articles)}] Processing: {article.get('title', 'Untitled')[:50]}...")
        
        # Check for actual content, not "success" key
        has_content = article.get("full_text", "").strip()
        char_count = article.get("char_count", 0)
        
        #  Skip articles with no meaningful content
        if not has_content or char_count < 100:
            print(f"    ⚠️ Skipping: No meaningful content ({char_count} chars)")
            summarized_articles.append({
                **article,
                "summary": "",
                "summary_status": "failed_no_content",
                "word_count": 0,
                "quality_check": "No"
            })
            continue
        
        title = article.get("title", "Unknown")
        full_text = article.get("full_text", "")
        rating = article.get("rating", article.get("llm_score", 0)) 
        
        # Check quality and summarize in one go
        prompt = f"""
        TASK: Analyze this article and create a high-quality summary.
        
        ARTICLE TITLE: {title}
        RELEVANCE SCORE: {rating}/100
        
        FULL ARTICLE TEXT (first 4000 chars):
        {full_text[:4000]}
        
        INSTRUCTIONS:
        1. First, CHECK QUALITY: Is this actual article content or just navigation/ads or Security or Privacy or Privacy Policy page or related to video? (Answer: Yes/No)
        2. If answer is No and quality is GOOD, create a CONCISE in 5-8 sentences summary.
        3. Focus on: Key points, main arguments, important facts.
        4. Write in clear, engaging language.
        5. Output format:
           QUALITY: [Yes/No]
           SUMMARY: [Your SUMMARY in 5-8 sentences summary  here]
        """
        
        try:
            response = llm.invoke(prompt)
            response_text = response.content
            
            # Parse response
            quality = "No"
            summary = ""
            
            # Extract quality check
            if "QUALITY: Yes" in response_text or "quality: yes" in response_text.lower():
                quality = "Yes"
            
            # Extract summary 
            summary_match = re.search(r'SUMMARY:\s*(.+)', response_text, re.DOTALL)
            if summary_match:
                summary = summary_match.group(1).strip()
            else:
                # take everything after QUALITY line
                lines = response_text.split('\n')
                in_summary = False
                summary_lines = []
                
                for line in lines:
                    if line.strip().startswith('SUMMARY:'):
                        in_summary = True
                        summary_lines.append(line.replace('SUMMARY:', '').strip())
                    elif in_summary and line.strip():
                        summary_lines.append(line.strip())
                
                summary = ' '.join(summary_lines)
            
            # Calculate word count
            word_count = len(summary.split())
            
            # Ensure 200 words
            if word_count > 200:
                # Trim to 200 words
                words = summary.split()[:200]
                summary = ' '.join(words)
                word_count = 200
            
            print(f"    ✅ Quality: {quality}, Summary: {word_count} words")
            
            summarized_articles.append({
                **article,
                "summary": summary,
                "summary_status": "success" if quality == "Yes" and word_count > 50 else "poor_quality",
                "quality_check": quality,
                "word_count": word_count,
                "original_length": len(full_text)
            })
            
        except Exception as e:
            print(f"    ❌ LLM failed: {e}")
            summarized_articles.append({
                **article,
                "summary": "",
                "summary_status": "llm_error",
                "quality_check": "Error",
                "word_count": 0
            })
    
    return summarized_articles




def summarizer_node(state: Dict[str, Any], llm) -> Dict[str, Any]:
    """Node: Summarize articles and check quality"""
    
    # Get articles from previous node
    full_articles = state.get("full_articles", [])
    
    if not full_articles:
        print("❌ No full_articles to summarize!")
        return {
            **state, 
            "messages": state.get("messages", []) + ["No articles to summarize"],
            "summarized_articles": [],
            "summary_stats": {"total": 0, "summarized": 0}
        }
    
    print(f"📝 SUMMARIZER NODE: Processing {len(full_articles)} articles")
    print("=" * 70)
    
    #  Call the summarizer agent
    summarized_articles = summarize_article_checker(full_articles, llm=llm)
    
    # Calculate statistics
    successful = [a for a in summarized_articles if a.get("summary_status") == "success"]
    good_quality = [a for a in summarized_articles if a.get("quality_check") == "Yes"]
    
    stats = {
        "total_articles": len(summarized_articles),
        "successfully_summarized": len(successful),
        "good_quality_content": len(good_quality),
        "success_rate": f"{(len(successful)/len(summarized_articles))*100:.1f}%",
        "average_word_count": sum(a.get("word_count", 0) for a in successful) / max(len(successful), 1)
    }
    
    # Show sample summaries
    if successful:
        print(f"\n✅ SUCCESSFUL SUMMARIES ({len(successful)} articles):")
        for i, article in enumerate(successful[:2], 1):  # Show first 2
            print(f"\n{i}. 📰 {article.get('title', 'Untitled')[:50]}...")
            print(f"   ⭐ Rating: {article.get('rating', 0)}/100")
            print(f"   📊 Quality: {article.get('quality_check', 'Unknown')}")
            print(f"   📝 Summary ({article.get('word_count', 0)} words):")
            print(f"   {article.get('summary', '')[:150]}...")
    
    # Return updated state
    return {
        **state,
        "summarized_articles": summarized_articles,
        "summary_stats": stats,
        "messages": [
            *state.get("messages", []),
            f"✅ Summarized {len(successful)}/{len(summarized_articles)} articles"
        ]
    }



def create_podcast_intro(top_articles, llm):
    """
    Creates podcast intro using ONLY titles and ratings
    Token-efficient: ~1 LLM call
    """
    
    # Prepare minimal data for LLM
    news_items = []
    for i, article in enumerate(top_articles[:3], 1):  # Top 3 for intro !!!
        title = article.get("title", "")
        rating = article.get("llm_score", 0) or article.get("rating", 0)
        news_items.append(f"{i}. {title} (Relevance: {rating}/100)")
    
    prompt = f"""You are a professional AI news podcast host. Create a 50-word podcast intro.

Today's Top AI News:
{chr(10).join(news_items)}

Intro Requirements:
- Start with "Welcome to Non-commercial AI Daily Digest!"
- Mention this is your AI news roundup
- Briefly highlight the key themes from today's headlines
- Sound engaging and professional
- Keep it under 100 words

Podcast Intro:"""
    
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        print(f"❌ Intro creation failed: {e}")
        return "Welcome to AI Daily Digest! In today's episode, we're covering the latest breakthroughs and debates in artificial intelligence."


def create_podcast_transitions(top_articles, llm):
    """
    Creates transitions between news items using ONLY titles
    Token-efficient: ~1 LLM call for all transitions
    """
    
    titles = [article.get("title", "") for article in top_articles]
    
    prompt = f"""Create natural podcast transitions between these news segments.
    
News Titles (in order):
{chr(10).join(f"{i+1}. {title}" for i, title in enumerate(titles))}

Requirements:
- Create 1-2 sentence transitions between each news item
- Make them sound natural and conversational
- Connect themes when possible (e.g., "Speaking of X, this relates to Y...")
- Don't summarize the articles, just transition between them
- Format as a numbered list: "1. [transition between #1 and #2]"

Transitions:"""
    
    try:
        response = llm.invoke(prompt)
        # Parse the transitions
        transitions_text = response.content.strip()
        transitions = []
        
        # Simple parsing
        lines = transitions_text.split('\n')
        for line in lines:
            line = line.strip()
            if line and line[0].isdigit() and '.' in line:
                transition = line.split('.', 1)[1].strip()
                transitions.append(transition)
        
        # Ensure we have enough transitions
        while len(transitions) < len(titles) - 1:
            transitions.append("Moving on to our next story...")
        
        return transitions[:len(titles)-1]  # N-1 transitions for N articles
        
    except Exception as e:
        print(f"❌ Transition creation failed: {e}")
        # Fallback transitions
        return ["Now, let's look at our next story..."] * (len(titles) - 1)


def build_podcast_script(intro, articles, transitions):
    """Builds podcast script using only articles with proper summaries"""
    
    script_parts = ["AI DAILY DIGEST - PODCAST SCRIPT", "", intro, ""]
    
    # 2. News Items - FILTER for articles with actual summaries
    for i, article in enumerate(articles):
        # Skip articles without proper summaries
        summary = article.get('summary', '').strip()
        if not summary:  # Skip empty summaries
            continue
            
        # Add article
        script_parts.append(f"\n STORY {i+1}: {article.get('title', 'Unknown Title')}.")
        script_parts.append("-")
        
        # Use the actual summary
        script_parts.append(summary)
        
        # Add transition if not last article and next article has summary
        if i < len(articles) - 1:
            next_summary = articles[i + 1].get('summary', '').strip()
            if next_summary:  # Only add transition if next article is valid
                script_parts.append("")
                script_parts.append(f"{transitions[i] if i < len(transitions) else 'Moving on...'}")
    
    # 3. Outro
    if len(script_parts) > 4:  # Only add outro if we added stories
        script_parts.append("\n=")
        script_parts.append("Thanks for listening to AI Daily Digest!")
        script_parts.append("Stay tuned for more AI news updates.")
        script_parts.append("=")
    
    return '\n'.join(script_parts)



def podcast_script_writer_node(state, llm):
    """
    Creates podcast script: Intro + News Blocks + Transitions
    Uses minimal tokens by processing only necessary data
    """
    
    print("\n" + "="*70)
    print("🎙️  PODCAST SCRIPT WRITER: Creating engaging podcast")
    print("="*70)
    
    # Get summarized articles
    summarized_articles = state.get("summarized_articles", [])

    if summarized_articles:
        print(f"📝 First summary has 'summary': {'summary' in summarized_articles[0]}")
        if 'summary' in summarized_articles[0]:
            summary = summarized_articles[0].get('summary', '')
            print(f"📏 Summary length: {len(summary)} chars, {len(summary.split())} words")
        print(f"🎯 Summary status: {summarized_articles[0].get('summary_status', 'unknown')}")
    
    if not summarized_articles:
        print("⚠️  No articles to create podcast from.")
        return {
            **state,
            "messages": state.get("messages", []) + ["Podcast: No input articles."]
        }
    
    # STEP 1: Select Top 10 Articles (by rating)
    successful_articles = [a for a in summarized_articles if a.get("summary_status") == "success"]
    print(f"📊 Found {len(successful_articles)} successful summaries out of {len(summarized_articles)} total")
    
    if not successful_articles:
        print("⚠️  No articles with 'success' status. Using all articles instead...")
        successful_articles = summarized_articles
    
    # Simple scoring - llm_score first, rating fallback
    top_articles = sorted(
        successful_articles,
        key=lambda x: x.get("llm_score", x.get("rating", 0)),  
        reverse=True
    )[:5]  # top articles !!!
    
    print(f"📊 Selected top {len(top_articles)} articles for podcast")
    
    # STEP 2: Create Podcast Intro (LLM Call #1)
    print("\n1️⃣ Creating podcast intro...")
    intro_text = create_podcast_intro(top_articles, llm)
    
    # STEP 3: Create Natural Transitions (LLM Call #2)
    print("\n2️⃣ Creating transitions between news items...")
    transitions = create_podcast_transitions(top_articles, llm)
    
    # STEP 4: Build Final Script
    print("\n3️⃣ Building final podcast script...")
    podcast_script = build_podcast_script(intro_text, top_articles, transitions)
    
    # STEP 5: Calculate total words/time
    total_words = len(podcast_script.split())
    estimated_minutes = total_words // 150  # 150 words/minute speaking rate // not used
    
    print(f"\n✅ Podcast Script Complete: {total_words} words (~{estimated_minutes} minutes)")
    
    # Return updated state
    return {
        **state,
        "podcast_script": podcast_script,
        "podcast_metadata": {
            "total_articles": len(top_articles),
            "total_words": total_words,
            "estimated_minutes": estimated_minutes,
            "top_article_titles": [a.get("title", "")[:50] for a in top_articles]
        },
        "messages": state.get("messages", []) + [
            f"✅ Podcast: Created {estimated_minutes}-minute script with {len(top_articles)} news items."
        ]
    }







# SEPARATE FUNCTIONS VERSION
def save_to_txt(podcast_script, filename_prefix="ai_podcast"):
    """Save podcast script to txt file"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{filename_prefix}_{today}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(podcast_script)
    
    print(f"📄 Saved: {filename}")
    return filename


def text_to_mp3(
    podcast_script: str,
    language: str = "en",
    filename_prefix: str = "ai_podcast"
) -> BytesIO:


    """Convert text to mp3 using gTTS"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{filename_prefix}_{today}.mp3"
    
    # Clean script for speech
    clean_text = podcast_script  # Limit for gTTS
    clean_text = clean_text.replace("[HOST] ", "").replace("[HOST]", "")
    
    tts = gTTS(text=clean_text, lang="en", slow=False)
    #tts.save(filename) # Removed saving to disk (Optional)

    # Virtual Part
    mp3_buffer = BytesIO()
    tts.write_to_fp(mp3_buffer)         
    mp3_buffer.seek(0)

    virtual_filename = f"{filename_prefix}_{today}.mp3"
    
    print(f"🎵 Created: {filename}")
    return filename, mp3_buffer





# Combined node using separate functions

def save_and_speak_node(state):
    """
    ✅ Saves podcast script to files AND generates audio
    """
    print("\n" + "="*60)
    print("💾 SAVE & SPEAK NODE: Creating files...")
    print("="*60)
    
    # Get the podcast script from previous node
    podcast_script = state.get("podcast_script", "")
    
    if not podcast_script:
        print("❌ No podcast script found!")
        return {
            **state,
            "messages": state.get("messages", []) + ["❌ No podcast script to save"]
        }
    
    # SAVE TO TEXT FILE
    txt_filename = save_to_txt(podcast_script)
    
    # CREATE MP3 AUDIO
    mp3_filename, audio_buffer = text_to_mp3(podcast_script) # Get both filename and buffer
    
    print("✅ Files created:")
    print(f"   📄 Text: {txt_filename}")
    print(f"   🎵 Audio: {mp3_filename}")


    state["audio_buffer"] = audio_buffer
    return {
        **state,
        "saved_files": {
            "txt_file": txt_filename,
            "mp3_file": mp3_filename,
            "script_length": len(podcast_script)
        },
        "messages": state.get("messages", []) + [
            f"✅ Saved podcast script ({len(podcast_script)} chars)",
            "✅ Created audio file"
        ]
    }


