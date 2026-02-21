import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")

# Default URLs
DEFAULT_URLS = [
    "https://www.therundown.ai",
    "https://www.artificialintelligence-news.com",
    "https://news.mit.edu/topic/artificial-intelligence2",
    "https://openai.com/blog",
    "https://venturebeat.com/category/ai",
    "https://techcrunch.com/tag/artificial-intelligence",
    "https://www.wired.com/tag/artificial-intelligence",
    "https://www.marktechpost.com",
]