

from typing import List, Dict, Optional, Any
from typing_extensions import TypedDict, Annotated
from io import BytesIO
from operator import add


class AgentState(TypedDict):
    """Complete state structure for the podcast workflow"""
    urls: Annotated[list[str], add]
    llm: Any
    results: List[Dict[str, Any]]
    messages: List[str]
    top_20_articles: List[Dict[str, Any]]
    route: str
    summary_method: str 
    full_articles: List[Dict[str, Any]]
    summarized_articles: List[Dict[str, Any]]
    summary_stats: Dict[str, Any]
    extraction_stats: Dict[str, Any]
    podcast_script: Optional[str]
    podcast_metadata: Dict[str, Any]
    saved_files: Dict[str, Any]
    human_feedback: str
    url_grade: str
    url_reasoning: str  
    audio_buffer: Optional[BytesIO]

