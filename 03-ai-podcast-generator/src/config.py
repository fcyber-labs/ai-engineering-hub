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


top50_urls = [
    "https://www.therundown.ai",                        # 1. The Rundown AI
    "https://www.artificialintelligence-news.com",      # 2
    "https://news.mit.edu/topic/artificial-intelligence2",  # 3. MIT News AI
    "https://openai.com/blog",                          # 4

    "https://venturebeat.com/category/ai",              # 7
    "https://techcrunch.com/tag/artificial-intelligence",  # 8
    "https://www.wired.com/tag/artificial-intelligence",   # 9
    "https://www.marktechpost.com",                     # 10
    "https://www.kdnuggets.com",                        # 11
    "https://towardsdatascience.com/tag/artificial-intelligence",  # 12
    "https://huggingface.co/blog",                      # 13
    "https://www.crescendo.ai/news",                    # 14
    "https://www.superhuman.ai",                        # 15
    "https://theresanaiforthat.com",                    # 16. TAAFT
    "https://www.theneurondaily.com",                   # 17. The Neuron
    "https://www.bensbites.com",                        # 18. Ben's Bites
    "https://bair.berkeley.edu/blog",                   # 19. Berkeley AI Research
    "https://hai.stanford.edu/ai-index",                # 20. Stanford HAI / AI Index
    "https://blogs.nvidia.com/blog/category/ai",        # 21. NVIDIA AI Blog
    "https://ai.meta.com/blog",                         # 22. Meta AI Blog
    "https://www.microsoft.com/en-us/ai/blog",          # 23. Microsoft AI Blog
    "https://machinelearningmastery.com",               # 24
    "https://syncedreview.com",                         # 25
    "https://www.theverge.com/ai-artificial-intelligence",  # 26. The Verge AI
    "https://arstechnica.com/tag/artificial-intelligence",  # 27. Ars Technica AI
    "https://spectrum.ieee.org/topic/artificial-intelligence",  # 28. IEEE Spectrum AI
    "https://www.nature.com/subjects/artificial-intelligence",  # 29. Nature AI
    "https://www.sciencedirect.com/topics/computer-science/artificial-intelligence",  # 30
    "https://www.ibm.com/blog/topics/artificial-intelligence",  # 31. IBM AI Blog
    "https://www.anthropic.com/news",                   # 32. Anthropic News
    "https://www.datacamp.com/blog",                    # 33 (AI section)
    "https://www.fast.ai/posts",                        # 34. fast.ai
    "https://www.lesswrong.com/tag/ai",                 # 35. LessWrong AI
    "https://www.alignmentforum.org",                   # 36
    "https://www.assemblyai.com/blog",                  # 37
    "https://www.latent.space",                         # 38. Latent Space newsletter/blog
    "https://thezvi.substack.com",                      # 39. Don't Worry About the Vase (AI safety/news)
    "https://www.interconnects.ai",                     # 40. Interconnects
    "https://www.deeplearning.ai/the-batch",            # 41. The Batch
    "https://importai.substack.com",                    # 42. Import AI
    "https://www.lastweekin.ai",                        # 43
    "https://emergentmind.com",                         # 44 (paper summaries)
    "https://www.ai-supremacy.com",                     # 45
    "https://www.mindstream.news",                      # 46
    "https://www.aifire.co",                            # 47
    "https://www.neatprompts.com",                      # 48
    "https://www.analyticsvidhya.com/blog/category/artificial-intelligence/feed",
    "https://www.aitrends.com/feed",
    "https://www.unite.ai/feed",
    "https://www.artificialintelligence-news.com/category/machine-learning/feed",
    "https://www.zdnet.com/topic/artificial-intelligence/rss.xml",
]

