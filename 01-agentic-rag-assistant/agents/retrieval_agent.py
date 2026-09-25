

### Retriever Grader

from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate




def create_retriever_grader(llm):
    """Define data model for document evaluation"""
    class GradeDocuments(BaseModel):
        """Grade whether a retrieved document is relevant to the user question."""

        relevant: Literal["yes", "no"] = Field(...,
            description="Is the document relevant to the question?"
        )
        reasoning: str = Field(  
            ...,
            description="Short explanation (1–2 sentences) why you chose this route"
        )

    structured_llm_grader = llm.with_structured_output(GradeDocuments)

    # Create prompt template containing system message and user question
    system = """You are a relevance grader for a company RAG system.

            Decide if a retrieved document chunk has information that helps to answer the user question.

            Rules:
            - Grade 'yes' if the chunk has facts, numbers, names or context that help answer the question, even partly.
            - Grade 'no' if the chunk is about something else, even when it shares a few words with the question.

            Now evaluate this document against the question:"""

    grade_prompt = ChatPromptTemplate(
        [
            ("system", system),
            ("human", "Retrieved document: \n\n {document} \n\n User question: {question}")
        ]
    )

    # Create document retrieval grader
    retrieval_grader = grade_prompt | structured_llm_grader
    return retrieval_grader


