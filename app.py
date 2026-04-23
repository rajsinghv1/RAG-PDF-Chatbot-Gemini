import streamlit as st
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings   
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# Load API key
load_dotenv()


# Extract text
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text


# Split text
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_text(text)


# Vector DB
def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"   
    )

    db = FAISS.from_texts(text_chunks, embedding=embeddings)
    db.save_local("faiss_index")


# LLM
def get_llm():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    prompt = PromptTemplate.from_template("""
    Answer the question as detailed as possible from the provided context.
    If the answer is not in the context, say:
    "answer is not available in the context"

    Context:
    {context}

    Question:
    {question}

    Answer:
    """)

    return model, prompt


# Query
def user_input(user_question):
    if not os.path.exists("faiss_index/index.faiss"):
        st.error("Please upload and process PDF first!")
        return

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(user_question, k=3)

    context = " ".join([doc.page_content for doc in docs])

    model, prompt = get_llm()

    final_prompt = prompt.format(
        context=context,
        question=user_question
    )

    response = model.invoke(final_prompt)

    st.write("### Reply:")
    st.write(response.content)


# 🎨 UI
def main():
    st.set_page_config(page_title="Chat PDF AI")
    st.header("📄 Chat with PDF using Gemini 💁")

    if "processed" not in st.session_state:
        st.session_state.processed = False

    with st.sidebar:
        st.title("📂 Upload PDF")
        pdf_docs = st.file_uploader(
            "Upload PDF files",
            accept_multiple_files=True
        )

        if st.button("🚀 Submit & Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF")
                return

            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.session_state.processed = True
                st.success("✅ Processing complete!")

    if st.session_state.processed:
        user_question = st.text_input("💬 Ask a question from your PDFs")

        if user_question:
            user_input(user_question)
    else:
        st.info("👈 Upload and process PDFs first")


if __name__ == "__main__":
    main()