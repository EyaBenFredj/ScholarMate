# 📚 ScholarMate – AI Research Paper Assistant

ScholarMate is an open-source, locally-running GenAI assistant that helps you **understand, analyze, and interact with research papers** using state-of-the-art language models, semantic search, and document parsing — all **100% free and private**.

> 🧠 Ask questions, get summaries, extract tables, generate flashcards — all from your own PDF research papers, with no paid API keys or cloud dependencies.

---

## 🎯 Features

✅ Upload any PDF research paper  
✅ Ask questions using RAG (retrieval-augmented generation)  
✅ Summarize entire sections (Abstract, Methods, Results, etc.)  
✅ ELI5 Mode: "Explain Like I’m 5" for simpler answers  
✅ Generate highlights and key insights  
✅ Create study flashcards (Q&A style)  
✅ Explain citations and references  
✅ Extract tables from PDF automatically  
✅ Compare two papers (similarity, methods, conclusions)  
✅ View full Q&A chat history  
✅ Fully offline – powered by [Ollama](https://ollama.com/) + FAISS + Streamlit

---

## 🧱 Project Structure

ScholarMate/
├── app.py # Streamlit app (main UI)
├── pdf_utils.py # PDF parsing: text, sections, tables
├── rag_pipeline.py # Embedding, RAG, summarization, flashcards, etc.
├── requirements.txt # Python dependencies

yaml
Copier le code

---

## 🛠️ Tech Stack

| Layer         | Tool / Library                      |
|---------------|-------------------------------------|
| 🧠 LLM         | [LLaMA3](https://ollama.com/library/llama3) via [Ollama](https://ollama.com) |
| 🔍 Embeddings  | SentenceTransformers (MiniLM)       |
| 📦 Vector DB   | FAISS (local, fast, open-source)    |
| 📄 PDF Parsing | PyMuPDF + pdfplumber                |
| 💬 UI          | Streamlit                           |
| 🧠 RAG Logic   | LangChain + custom prompt design     |

---

## 🚀 Installation Guide (Windows / Linux / macOS)

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ScholarMate.git
cd ScholarMate
2. Set Up Python Environment
bash
Copier le code
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on macOS/Linux
3. Install Dependencies
bash
Copier le code
pip install -r requirements.txt
4. Install and Start Ollama (Local LLM)
Download and install Ollama

Pull a model:

bash
Copier le code
ollama pull llama3
Run the model:

bash
Copier le code
ollama run llama3
Leave that terminal open – it runs your LLM backend locally.

5. Run ScholarMate
In a separate terminal (with virtual env activated):

bash
Copier le code
streamlit run app.py
Open http://localhost:8501 in your browser.

🧪 Usage Examples
"Summarize the abstract"

"What is the main contribution of the paper?"

"Explain the method section like I'm 5"

"List key findings"

"Create flashcards for this paper"

"Compare this paper with another one"

"Extract tables with results"

🛡️ Privacy & Cost
💰 Free forever – no OpenAI or cloud API keys required

🔒 100% private – runs entirely on your device

📶 Offline-capable – LLM inference and vector search are local

📌 Roadmap
 Export chat history as PDF / Markdown

 Summarize citations with links to external databases

 Add Whisper or voice interface for spoken Q&A

 Deploy to Hugging Face Spaces (optional cloud demo)

🙌 Contributing
This is an open project!
Feel free to:

Suggest new features

Improve prompts

Add better section detection

Help with UI polish or deployment

📄 License
MIT License – feel free to use and adapt.

✨ Credits
LLaMA 3 by Meta

Ollama – local LLM runner

LangChain – RAG pipeline framework

SentenceTransformers – powerful open-source embeddings

Streamlit – fast ML app UI

💬 Contact / Feedback
Built by [Your Name]
Find me on LinkedIn or GitHub

yaml
Copier le code

---

✅ You can now paste this directly into your `README.md`.  
Let me know if you want help:
- Replacing your name and links
- Deploying it online
- Writing a LinkedIn post or GitHub release

You’ve got something special here.
