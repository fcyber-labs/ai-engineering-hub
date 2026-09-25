
### Answer generation

import os


def create_generate_answer(state, llm):
    """generate the answer"""
    question = state["question"]
    documents = state.get("documents", [])
    feedback = state.get("grade_feedback", "")
    
    # Combine documents, every chunk starts with the file it came from
    context = "\n\n".join([
        f"[Source: {os.path.basename(doc.metadata.get('source', 'unknown'))}]\n{doc.page_content}"
        for doc in documents
    ]) if documents else ""
    
    # Prompt
    prompt = f"""Answer this question using ONLY the data below:

    QUESTION: {question}

    FEEDBACK ON PREVIOUS ATTEMPT if provided: {feedback}

    AVAILABLE DATA: {context}

    Rules:
    - Do not use anything that is not in the data.
    - If the data does not have the answer, say: "I don't know based on the documents."
    - End your answer with a line "Sources:" and the file names you used.

    Your answer:"""
    
    answer = llm.invoke(prompt)  
    return {"answer": answer.content}