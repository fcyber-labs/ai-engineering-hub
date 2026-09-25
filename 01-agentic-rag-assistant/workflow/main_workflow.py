### Main Workflow



from langgraph.graph import StateGraph, END


from nodes.nodes import route_question_node, node_retrieve, grade_retrieval_node, generate_answer_node, grade_hallucination_node, grade_answer_node, rewrite_query_node, general_chat_node, clarify_node, final_respond_node
from core.state import GraphState


# Define workflow
workflow = StateGraph(GraphState)

# Add nodes
workflow.add_node("route_question", route_question_node)
workflow.add_node("general_chat", general_chat_node)
workflow.add_node("clarify", clarify_node)
workflow.add_node("retrieve", node_retrieve)
workflow.add_node("grade_retrieval", grade_retrieval_node)
workflow.add_node("generate_answer", generate_answer_node)
workflow.add_node("hallucination_check", grade_hallucination_node)
workflow.add_node("grade_answer", grade_answer_node)
workflow.add_node("rewrite_query", rewrite_query_node)
workflow.add_node("final_respond", final_respond_node)


workflow.set_entry_point("route_question")

workflow.add_conditional_edges(
    "route_question",
    lambda state: state.get("route", "retrieve"),
    {
        "retrieve": "retrieve",
        "off_topic": "general_chat", 
        "clarify": "clarify"
    }
)


workflow.add_edge("retrieve","grade_retrieval")

workflow.add_conditional_edges(
    "grade_retrieval",
    lambda state: state.get("route", "bad"),  
    {
        "good": "generate_answer",
        "bad": "rewrite_query" 
    }
)


workflow.add_edge("generate_answer","hallucination_check")
workflow.add_conditional_edges(
    "hallucination_check",
    lambda state: state.get("hallucination_route", "good"),
    {
        "good": "grade_answer",
        "hallucinated": "rewrite_query"
    }
)
workflow.add_conditional_edges(
    "rewrite_query",
    lambda state: "clarify" if state.get("rewrite_count", 0) >= 3 else "retrieve",
    {
        "retrieve": "retrieve",
        "clarify": "clarify"
    }
)

workflow.add_conditional_edges(
    "grade_answer",
    lambda state: state.get("next", "generate_answer"), 
    {
        "final_respond": "final_respond",
        "generate_answer": "generate_answer"
    }
)

workflow.add_edge("general_chat", END)
workflow.add_edge("clarify", END)
workflow.add_edge("final_respond", END)

graph_app = workflow.compile(debug=True)
graph_app