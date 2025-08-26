
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

```

ScholarMate/
├── app.py              # Streamlit app (main UI)
├── pdf\_utils.py        # PDF parsing: text, sections, tables
├── rag\_pipeline.py     # Embedding, RAG, summarization, flashcards, etc.
├── requirements.txt    # Python dependencies

````

---

## 🛠️ Tech Stack

| Layer         | Tool / Library                                      |
|---------------|-----------------------------------------------------|
| 🧠 LLM         | [LLaMA3](https://ollama.com/library/llama3) via [Ollama](https://ollama.com) |
| 🔍 Embeddings  | SentenceTransformers (MiniLM)                       |
| 📦 Vector DB   | FAISS (local, fast, open-source)                    |
| 📄 PDF Parsing | PyMuPDF + pdfplumber                                |
| 💬 UI          | Streamlit                                           |
| 🧠 RAG Logic   | LangChain + custom prompt design                    |

---

## 🚀 Installation Guide (Windows / Linux / macOS)

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ScholarMate.git
cd ScholarMate
````

### 2. Set Up Python Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Start Ollama (Local LLM)

* Download and install [Ollama](https://ollama.com)
* Pull a model:

```bash
ollama pull llama3
```

* Run the model:

```bash
ollama run llama3
```

> 📝 Leave that terminal open – it runs your LLM backend locally.

### 5. Run ScholarMate

In a **separate terminal** (with virtual environment activated):

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧪 Usage Examples

* `"Summarize the abstract"`
* `"What is the main contribution of the paper?"`
* `"Explain the method section like I'm 5"`
* `"List key findings"`
* `"Create flashcards for this paper"`
* `"Compare this paper with another one"`
* `"Extract tables with results"`

