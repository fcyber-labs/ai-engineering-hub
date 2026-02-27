from langgraph.graph import StateGraph, END
from .nodes import scraper_rate_node, content_extractor_node, summarizer_node, podcast_script_writer_node, save_and_speak_node, summarize_bart_node, summary_router
from .state import AgentState


workflow = StateGraph(AgentState)



workflow.add_node("scraper_rate_node", scraper_rate_node)
workflow.add_node("content_extractor_node", content_extractor_node)
workflow.add_node("summarizer_node", summarizer_node)
workflow.add_node("podcast_script_writer_node", podcast_script_writer_node)

workflow.add_node("save_and_speak_node", save_and_speak_node)
workflow.add_node("summarize_bart_node", summarize_bart_node)
workflow.add_node("summary_router", summary_router)


workflow.set_entry_point("scraper_rate_node")

workflow.add_edge("scraper_rate_node","content_extractor_node")


workflow.add_conditional_edges(
    "content_extractor_node", 
    summary_router,
    {
        "summarizer_node": "summarizer_node",
        "summarize_bart_node": "summarize_bart_node"
    }
)

workflow.add_edge("summarizer_node","podcast_script_writer_node")
workflow.add_edge("summarize_bart_node","podcast_script_writer_node")
workflow.add_edge("podcast_script_writer_node", "save_and_speak_node")


workflow.add_edge("save_and_speak_node", END)
graph_app = workflow.compile(debug=True)



