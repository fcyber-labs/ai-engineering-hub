import gradio as gr
import time
from workflow.main_workflow import graph_app

class LangGraphChatInterface:
    def __init__(self, graph_app, config=None):
        self.graph_app = graph_app
        self.config = config or {"configurable": {"thread_id": "demo_user_1"}}
        self.conversation_history = []
    
    def process_question(self, question: str, chat_history: list) -> tuple:
        """Process a question through the LangGraph workflow"""
        print(f"\n{'='*50}")
        print(f"Processing: {question}")
        print(f"{'='*50}")
        
        start_time = time.time()
        
        # Initialize state, should mathc full workflow state 
        initial_state = {
            "question": question,
            "normalized_question": question,
            "generation": "",
            "final_answer": "",
            "transform_count": 0,
            "retrieval_count": 0,
            "retrieved_docs": [],
            "filtered_docs": [],
            "context_docs": [],
            "answer": "",
            "citations": [],
            "needs_clarification": False,
            "clarification_question": "",
            "max_retries_reached": False
        }
        
        # Run the graph
        try:
            # Create unique thread ID
            import random
            thread_id = f"user_{int(time.time())}_{random.randint(1000, 9999)}"
            config = {"configurable": {"thread_id": thread_id}}
            
            print("Invoking full LangGraph workflow...")
            final_state = self.graph_app.invoke(
                initial_state,
                config=config
            )
            
            # Extract answer
            answer = ""
            if "answer" in final_state and final_state["answer"]:
                answer = final_state["answer"]
                print(f"✅ Found answer in 'answer': {answer[:100]}...")
            elif "final_answer" in final_state and final_state["final_answer"]:
                answer = final_state["final_answer"]
                print(f"✅ Found answer in 'final_answer': {answer[:100]}...")
            elif "generation" in final_state and final_state["generation"]:
                answer = final_state["generation"]
                print(f"✅ Found answer in 'generation': {answer[:100]}...")
            else:
                answer = "I couldn't generate an answer."
                print("❌ No answer found")
            
            # Get other info
            retrieval_count = 0
            
            # Check different document fields
            if "retrieved_docs" in final_state and final_state["retrieved_docs"]:
                retrieval_count = len(final_state["retrieved_docs"])
            elif "documents" in final_state and final_state["documents"]:
                retrieval_count = len(final_state["documents"])
            elif "filtered_docs" in final_state and final_state["filtered_docs"]:
                retrieval_count = len(final_state["filtered_docs"])
            elif "context_docs" in final_state and final_state["context_docs"]:
                retrieval_count = len(final_state["context_docs"])
            else:
                # Fallback to state field if no actual docs found
                retrieval_count = final_state.get("retrieval_count", 0)
            
            processing_time = time.time() - start_time
            
        except Exception as e:
            print(f"❌ Graph execution error: {e}")
            import traceback
            traceback.print_exc()
            answer = f"Error: {str(e)[:100]}"
            retrieval_count = 0
            processing_time = time.time() - start_time
        
        # Add to conversation history
        self.conversation_history.append({
            "question": question,
            "answer": answer,
            "retrieval_count": retrieval_count,
            "time": processing_time
        })
        
        # Format chat history
        chat_history.append({"role": "user", "content": question})
        chat_history.append({"role": "assistant", "content": answer})
        
        # Prepare debug info
        debug_info = self._prepare_debug_info(
            retrieval_count, processing_time, answer
        )
        
        return chat_history, debug_info, ""
    
    def _prepare_debug_info(self, retrieval_count: int, 
                          processing_time: float, answer: str) -> str:
        """Prepare debug information"""
        debug_text = f"**Processing Time:** {processing_time:.2f} seconds\n"
        debug_text += f"**Retrieved Documents:** {retrieval_count}\n"
        debug_text += "**Workflow:** Full LangGraph\n\n"
        
        # Add answer preview
        debug_text += f"**Answer:**\n{answer[:500]}"
        if len(answer) > 500:
            debug_text += "..."
        
        return debug_text
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        return [], "", ""

# Initialize with your fukk graph_app
chat_interface = LangGraphChatInterface(graph_app)

# Gradio interface
def gradio_chat(question, chat_history):
    """Gradio chat interface function"""
    return chat_interface.process_question(question, chat_history)

def clear_chat():
    """Clear the chat"""
    return chat_interface.clear_history()

# Create Gradio interface
with gr.Blocks(title="Agentic RAG Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 👨‍💼 Agentic RAG Assistant")
    gr.Markdown("Smart Q&A Assistant with intelligent routing, query refinement, hallucination checking, self-correction loops, and hybrid retrieval")
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                label="Conversation",
                height=400,

            )
            
            question_input = gr.Textbox(
                label="Type your question",
                placeholder="Ask about TechNova...",
                lines=2
            )
            
            with gr.Row():
                submit_btn = gr.Button("Send", variant="primary")
                clear_btn = gr.Button("Clear Chat", variant="secondary")
            
            debug_output = gr.Markdown(label="Workflow Details")
        
        with gr.Column(scale=1):
            gr.Markdown("## 📋 Features")
            gr.Markdown("""
            **Complete workflow:**
            - Smart question routing
            - Query transformation
            - Document retrieval & grading
            - Answer generation
            - Quality checking
            - Hallucination checking
            - Self-correction loops

            **Powered by:**
            - LangGraph workflow
            - Debug mode enabled
            """)
            
            # Stats
            stats_markdown = gr.Markdown("## 📊 Stats\n\nNo conversations yet.")
            
            def update_stats():
                conv_count = len(chat_interface.conversation_history)
                if conv_count > 0:
                    latest = chat_interface.conversation_history[-1]
                    stats_text = "## 📊 Stats\n\n"
                    stats_text += f"**Total Queries:** {conv_count}\n"
                    stats_text += f"**Last Query Time:** {latest['time']:.2f}s\n"
                    stats_text += f"**Last Retrieval:** {latest['retrieval_count']} docs"
                    return stats_text
                return "## 📊 Stats\n\nNo conversations yet."
    
    # Example questions
    gr.Examples(
        examples=[
            ["Who founded TechNova?"],
            ["What products does TechNova make?"],
            ["A Brief History of TechNova"],
            ["Who are the key employees?"],
            ["What services do you offer?"],
            ["Create very brief analysis of the latest balance sheet"],

            ["What does the mix of enterprise, mid-market, and SMB clients suggest about TechNova's market strategy?"],
            ["What was the name of the flagship product developed after the seed funding?"]


        ],
        inputs=question_input,
        label="Try these questions:"
    )
    
    # Event handlers
    submit_btn.click(
        fn=gradio_chat,
        inputs=[question_input, chatbot],
        outputs=[chatbot, debug_output, question_input]
    ).then(
        fn=update_stats,
        outputs=stats_markdown
    )
    
    question_input.submit(
        fn=gradio_chat,
        inputs=[question_input, chatbot],
        outputs=[chatbot, debug_output, question_input]
    ).then(
        fn=update_stats,
        outputs=stats_markdown
    )
    
    clear_btn.click(
        fn=clear_chat,
        outputs=[chatbot, debug_output, question_input]
    ).then(
        fn=update_stats,
        outputs=stats_markdown
    )

print("Launching FULL LangGraph Assistant...")
print("Using complete workflow")
print("Debug mode: ON")

# Launch
if __name__ == "__main__":
    demo.launch(share=True, debug=True)


#
