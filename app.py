# app.py

import streamlit as st
import os
import tempfile

from pdf_utils import extract_text_from_pdf, extract_sections, extract_tables_from_pdf
from rag_pipeline import (
    split_text, build_faiss_index, answer_query, summarize_section,
    generate_flashcards, extract_key_points, explain_citations, compare_papers
)

st.set_page_config(page_title="📚 ScholarMate", layout="wide")
st.title("📚 ScholarMate – AI Research Assistant")

# Session state for Q&A memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

tab1, tab2, tab3 = st.tabs(["🧠 Analyze One Paper", "🆚 Compare Two Papers", "📤 Export & Tables"])

with tab1:
    st.subheader("Upload and explore a research paper")
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        full_text = extract_text_from_pdf(pdf_path)
        sections = extract_sections(full_text)
        chunks = split_text(full_text)
        db = build_faiss_index(chunks)

        st.success("Paper processed. Ready to explore!")

        col1, col2 = st.columns(2)
        with col1:
            question = st.text_input("Ask a question about the paper:")
            simplify = st.checkbox("Explain like I'm 5 (ELI5)", key="eli5")

            if question:
                answer = answer_query(db, question, simplify=simplify)
                st.session_state.chat_history.append((question, answer))
                st.markdown("**Answer:**")
                st.write(answer)

        with col2:
            section = st.selectbox("Summarize a section", list(sections.keys()))
            if st.button("Summarize Section"):
                summary = summarize_section(sections[section], simplify=simplify)
                st.markdown("**Summary:**")
                st.write(summary)

        st.markdown("---")
        st.subheader("🧠 More Tools")

        if st.button("📌 Generate Key Insights"):
            highlights = extract_key_points(full_text)
            st.write(highlights)

        if st.button("🃏 Generate Flashcards"):
            cards = generate_flashcards(full_text)
            st.write(cards)

        if st.button("🔗 Explain Citations"):
            cites = explain_citations(full_text)
            st.write(cites)

        st.markdown("---")
        st.subheader("🗂️ Q&A History")
        for q, a in st.session_state.chat_history:
            st.markdown(f"**Q:** {q}")
            st.markdown(f"**A:** {a}")

with tab2:
    st.subheader("Compare Two Papers")
    file1 = st.file_uploader("Upload Paper 1", type=["pdf"], key="p1")
    file2 = st.file_uploader("Upload Paper 2", type=["pdf"], key="p2")

    if file1 and file2:
        with tempfile.NamedTemporaryFile(delete=False) as tmp1, tempfile.NamedTemporaryFile(delete=False) as tmp2:
            tmp1.write(file1.read())
            tmp2.write(file2.read())
            text1 = extract_text_from_pdf(tmp1.name)
            text2 = extract_text_from_pdf(tmp2.name)

        if st.button("🔍 Compare Papers"):
            comparison = compare_papers(text1, text2)
            st.write(comparison)

with tab3:
    st.subheader("📊 Extract Tables")
    table_file = st.file_uploader("Upload a PDF to extract tables", type=["pdf"], key="table_pdf")
    if table_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(table_file.read())
            tables = extract_tables_from_pdf(tmp.name)

        for i, table in enumerate(tables):
            st.markdown(f"**Table {i+1}**")
            st.table(table)

    st.markdown("📝 Coming Soon: Export Q&A & notes to PDF or DOCX.")
