### Adding Hallucination Checker for Responses

# define data model for hallucination check

from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field



def create_hallucination_grader(llm):
    """define data model for hallucination check"""
    class GradeHallucinations(BaseModel):
        """Evaluate hallucinations."""

        grounded: Literal["yes", "no"] = Field(
            description="Is answer grounded?"
        )

        reasoning: str = Field(
            description="Brief reasoning"
        )

        
    # Initialize LLM with function calling
    structured_llm_grader = llm.with_structured_output(GradeHallucinations)

    # Very simple prompt
    system_prompt = """Check if the answer is backed by the documents.
                    Say 'yes' when every fact in the answer can be found in the documents (other wording is fine).
                    Say 'no' when the answer says something the documents do not say, or when it contradicts them.
                    An answer that only says it does not know counts as 'yes'."""
    
    hallucination_prompt = ChatPromptTemplate(
        [
            ("system", system_prompt),
            ("human", "Docs: {documents} \n Answer: {generation}")
        ]
    )

    hallucination_grader = hallucination_prompt | structured_llm_grader
    return hallucination_grader