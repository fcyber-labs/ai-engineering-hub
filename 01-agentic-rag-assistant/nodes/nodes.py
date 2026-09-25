

### Nodes

from agents.answer_grader_agent import create_answer_grader
from agents.correction_agent import create_question_checker
from agents.generation_agent import create_generate_answer
from agents.hallucination_agent import create_hallucination_grader
from agents.retrieval_agent import create_retriever_grader
from agents.query_rewriter_agent import create_query_rewriter
from data.embeddings import hybrid_retrieve_func

from config.settings import llm
from core.state import GraphState

#   Node: Question Router

def route_question_node(state: GraphState) -> GraphState:
    """Route the question"""
    question = state["question"]
    

    router_chain = create_question_checker(llm)
    decision = router_chain.invoke({"question": question})
    
    # Convert LLM decision 
    if decision.route == "vectorstore":
        return {"route": "retrieve"}     
    elif decision.route == "general_chat":
        return {"route": "off_topic"} 
    else:  
        return {"route": "clarify"} 


#   Node: Retrieve

def node_retrieve(state: GraphState) -> GraphState:
    """ hybrid_retrieve_func """
    question = state["question"]
    
    documents = hybrid_retrieve_func(question)
    
    return {
        "documents": documents, 
        "route": "grade_retrieval"
    }



#   Node: Retrieval Grader

# Option 1: Change grade_retrieval_node to return "bad"
def grade_retrieval_node(state: GraphState) -> GraphState:
    """Grade every retrieved document and keep only the relevant ones"""
    documents = state.get("documents", [])
    question = state.get("question", "")
    
    grader = create_retriever_grader(llm)
    
    if documents:
        # one grader call per document, batch runs a few of them side by side
        grades = grader.batch(
            [{"document": doc.page_content, "question": question} for doc in documents],
            config={"max_concurrency": 3}
        )
        relevant_docs = [doc for doc, grade in zip(documents, grades) if grade.relevant == "yes"]
        
        if relevant_docs:
            # only these go on to the answer generation
            return {"documents": relevant_docs, "retrieval_grade": "good", "route": "good"}
    
    return {"retrieval_grade": "bad", "route": "bad"}


#   Node: Generate Answer




def generate_answer_node(state: GraphState) -> GraphState:
    """Node that generates answer using ensemble"""
    # Ensemble logic 
    result = create_generate_answer(state, llm)  
    
    generated_answer = result.get("answer", "")
    
    # If answer is empty or short
    if not generated_answer or len(generated_answer.strip()) < 10:
        print(f"Warning: Generated answer too short: '{generated_answer}'")
        # Create a simple fallback
        question = state.get("question", "the question")
        generated_answer = f"I'm working on answering: {question}. Let me provide you with the information from our documents."
    
    return {
        "generation": generated_answer,
        "route": "hallucination_check"
    }

#   Node: Hallucination Grader



def grade_hallucination_node(state: GraphState) -> GraphState:
    """Node for hallucination check"""
    generation = state.get("generation", "")
    documents = state.get("documents", [])
    
    # Quick check - if no real content, return good
    if not generation or len(generation.strip()) < 10:
        return {"hallucination_route": "good"}
    
    # all documents and the whole answer, nothing is cut
    context = "\n\n".join([doc.page_content for doc in documents]) if documents else "No docs"
    
    # the llm can fail (rate limit, timeout), so we try twice
    result = None
    for attempt in (1, 2):
        try:
            hallucination_grader = create_hallucination_grader(llm)
            result = hallucination_grader.invoke({
                "documents": context,
                "generation": generation
            })
            break
        except Exception as e:
            print(f"Hallucination check failed (try {attempt} of 2): {e}")
    
    # could not check it, so don't let it pass quietly, tell the user
    if result is None:
        note = "\n\n(I couldn't check this answer against the documents.)"
        return {"hallucination_route": "good", "generation": generation + note}
    
    # trust the grader
    if result.grounded == "no":
        print(f"Hallucination: {result.reasoning}")
        return {"hallucination_route": "hallucinated"}
    
    return {"hallucination_route": "good"}



#   Node: Answer Grader

def grade_answer_node(state: GraphState) -> GraphState:
    """Grade answer and store feedback"""
    attempts = state.get("attempts", 0) + 1
    
    answer_grader = create_answer_grader(llm)
    result = answer_grader.invoke({
        "question": state["question"],
        "generation": state.get("generation", "")
    })
    
    if result.addresses_answer == "yes":
        return {"next": "final_respond", "attempts": attempts}
    else:

        return {
            "next": "generate_answer", 
            "attempts": attempts,
            "grade_feedback": result.reasoning  
        }


#   Node: Query Rewriter

def rewrite_query_node(state: GraphState) -> GraphState:
    """Rewrite the query after answer generation check"""
    question = state["question"]
    
    rewriter = create_query_rewriter(llm)
    new_question = rewriter.invoke({"question": question})
    
    return {
        "question": new_question,
        "rewrite_count": state.get("rewrite_count", 0) + 1,
        "route": "retrieve"
    }

#   Node: General chat

def general_chat_node(state: GraphState) -> GraphState:
    """Generate general answer to the question not related to the company"""

    
    answer = "This is not related to the company."
    return {
        "generation": answer,
        "final_answer": answer
    }

#   Node: Clarify node

def clarify_node(state: GraphState) -> GraphState:
    """Ask to clarify the question"""
    answer = "I need more details to answer your question. Could you please clarify or rephrase your question?"
    
    return {
        "generation": answer,
        "final_answer": answer,
        "route": "end"  
    }

#   Node: Final respond

def final_respond_node(state: GraphState) -> GraphState:
    """Return final answer"""
    answer = state.get("generation", "No answer generated.").strip()
    
    return {
        "generation": answer,
        "route": "end"
    }