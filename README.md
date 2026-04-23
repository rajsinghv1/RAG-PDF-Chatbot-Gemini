# 📄 RAG PDF Chatbot using Gemini AI

## 🚀 Overview  
This project is an AI-powered chatbot that allows users to upload PDF documents and ask questions about their content in natural language.

Instead of simply searching text, the system uses **Retrieval-Augmented Generation (RAG)** — a technique that combines:
- 🔍 **Semantic search** (to find relevant content from PDFs)
- 🤖 **LLM generation (Gemini AI)** (to generate accurate answers)

This ensures responses are **context-based, relevant, and reliable**, not random AI guesses.

---

## 🧠 Tech Stack  

- **Python** – Core development  
- **Streamlit** – Interactive web interface  
- **LangChain** – LLM workflow management  
- **FAISS** – Vector database for fast similarity search  
- **HuggingFace Embeddings** – Convert text into vectors  
- **Google Gemini API** – Answer generation (LLM)  
- **PyPDF2** – Extract text from PDFs  

---

## ⚙️ Features  

- 📂 Upload and process multiple PDFs  
- 🔍 Automatic text extraction from documents  
- ✂️ Smart text chunking for better understanding  
- 🧠 Semantic search (meaning-based, not keyword-based)  
- 🤖 Context-aware answers using Gemini AI  
- ⚡ Fast and simple user interface  

---

## 📊 How It Works (Step-by-Step)

1. **Upload PDFs**  
   User uploads one or more PDF files.

2. **Text Extraction**  
   The system reads and extracts text from all pages.

3. **Chunking**  
   Large text is divided into smaller chunks for better processing.

4. **Embedding Creation**  
   Each chunk is converted into a vector using HuggingFace embeddings.

5. **Storage (FAISS)**  
   These vectors are stored in a vector database for fast retrieval.

6. **User Query**  
   User asks a question in natural language.

7. **Similarity Search**  
   The system finds the most relevant text chunks related to the query.

8. **Answer Generation (Gemini)**  
   Relevant context + question → sent to Gemini → final answer generated.

---

## 🎯 Use Cases  

- 📚 Study Assistant (notes, books, PDFs)  
- 🧠 Research Paper Analysis  
- 📄 Document Question Answering  
- 📊 Business Report Insights  
- 🏢 Knowledge Assistant for organizations  

---

## 📸 Demo  

Add your screenshot here:  
/screenshots/Chat_Result.png  

---

## ⭐ Future Improvements  

- 💬 Chat history (memory-based conversations)  
- 📑 Multi-document filtering  
- ☁️ Cloud deployment  
- 🎙️ Voice input support  
- 🔍 Hybrid search (keyword + semantic)  

---

## 📌 Key Highlights  

- Built a complete **RAG pipeline from scratch**  
- Integrated **LLM + Vector Database + UI**  
- Solves real-world problem: **document intelligence**  
- Suitable for **AI Engineer / Data Science roles**  

---

## ⭐ Support  

If you find this project useful:  
- Star ⭐ the repository  
