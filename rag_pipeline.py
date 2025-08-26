# rag_pipeline.py

from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import google.generativeai as genai
import os

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Set your Gemini API key
GENAI_API_KEY = os.getenv("GEMINI_API_KEY") or "your-api-key-here"
genai.configure(api_key=GENAI_API_KEY)

# Initialize Gemini model
gemini_model = genai.GenerativeModel("gemini-pro")

def split_text(text, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)

def build_faiss_index(chunks):
    return FAISS.from_texts(chunks, embedding_model)

def generate_answer_gemini(prompt):
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def answer_query(db, query, k=3, simplify=False):
    docs = db.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    mode = "Explain this simply like I'm 5.\n\n" if simplify else ""
    prompt = f"{mode}Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    return generate_answer_gemini(prompt)

def summarize_section(section_text, simplify=False):
    prompt = "Explain this section like I’m 5.\n\n" if simplify else "Summarize this section of a research paper.\n\n"
    prompt += section_text
    return generate_answer_gemini(prompt)

def generate_flashcards(text):
    prompt = f"Generate 5 flashcards (question-answer format) based on this paper:\n\n{text}"
    return generate_answer_gemini(prompt)

def extract_key_points(text):
    prompt = f"Extract 5 key findings or insights from this research paper:\n\n{text}"
    return generate_answer_gemini(prompt)

def explain_citations(text):
    prompt = f"Explain what the citations in this paper are referring to. Be brief and helpful:\n\n{text}"
    return generate_answer_gemini(prompt)

def compare_papers(text1, text2):
    prompt = f"Compare these two research papers in terms of topic, methods, and conclusions:\n\nPaper 1:\n{text1[:3000]}\n\nPaper 2:\n{text2[:3000]}"
    return generate_answer_gemini(prompt)
