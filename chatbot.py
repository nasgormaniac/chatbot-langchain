from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
import gradio as gr

from dotenv import load_dotenv
load_dotenv()

DATA_PATH = r"documents"
CHROMA_PATH = r"chroma_db"

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

llm = ChatGroq(
    model = "llama-3.1-8b-instant"
)

vector_store = Chroma(
    collection_name="chatbot_collection",
    embedding_function=embedding_model,
    persist_directory=CHROMA_PATH,
)

num_results = 3
retriever = vector_store.as_retriever(search_kwargs={'k':num_results})

def stream_response(message, history):
    docs = retriever.invoke(message)

    knowledge = ""

    for doc in docs:
        knowledge += doc.page_content+"\n\n"

        if message is not None:
            partial_message = ""

            rag_propmpt = f"""
            You are an assistent which answers questions based on knowledge which is provided to you.
            While answering, you don't use your internal knowledge, 
            but solely the information in the "The knowledge" section.
            You don't mention anything to the user about the povided knowledge.

            The question: {message}

            Conversation history: {history}

            The knowledge: {knowledge} 
            """

            for response in llm.stream(rag_propmpt):
                partial_message += response.content
                yield partial_message

chatbot = gr.ChatInterface(stream_response, textbox=gr.Textbox(
    placeholder="Tanya apa aja...",
    container=False,
    autoscroll=True,
    scale=7),
)

chatbot.launch()