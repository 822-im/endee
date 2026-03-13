# Endee Vector Search RAG Assistant

An AI-powered assistant built using **Retrieval Augmented Generation (RAG)** and **vector embeddings** to provide accurate and context-aware answers to user queries.

This project demonstrates how modern AI systems combine **semantic search and large language models** to build intelligent assistants similar to tools like ChatGPT or AI search engines.

The application retrieves relevant information using vector similarity search and then generates a meaningful answer using a large language model.

---

# Project Overview

Large language models are powerful, but they sometimes produce incorrect or outdated responses because they rely only on their training data.

To solve this problem, this project uses **Retrieval Augmented Generation (RAG)**.

Instead of answering a question directly, the system first retrieves the most relevant information from a knowledge base and then provides that information to the language model to generate a more accurate answer.

This approach improves reliability and makes the AI system more context-aware.

---

# How the System Works

The assistant follows a **RAG pipeline**:

User Question  
↓  
Convert question into embedding (Sentence Transformers)  
↓  
Vector similarity search  
↓  
Retrieve relevant context from knowledge base  
↓  
Send context to Large Language Model (Groq Llama Model)  
↓  
Generate final answer  

This pipeline ensures that responses are based on **relevant retrieved knowledge rather than guessing**.

---

# Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| Sentence Transformers | Generate vector embeddings for semantic search |
| NumPy | Perform vector similarity calculations |
| Groq API | Large language model for response generation |

---

# Key Features

• Retrieval Augmented Generation (RAG) architecture  
• Semantic search using vector embeddings  
• AI assistant style chat interface  
• Context-aware responses  
• Clean and responsive Streamlit UI  
• Integration with Groq LLM for natural language answers  

---

# Knowledge Base

The assistant retrieves information from a knowledge base stored in **knowledge.txt**.

The text is converted into **vector embeddings**, allowing the system to perform semantic similarity search and identify the most relevant information for each user query.

---

# 📂 Project Structure
AI-RAG-Knowledge-Assistant
│
├── app.py
├── knowledge.txt
├── requirements.txt
└── README.md

## ▶️ Run the Project

1. Clone the repository
git clone https://github.com/your_username/AI-RAG-Knowledge-Assistant.git


2. Install dependencies
pip install -r requirements.txt


3. Add your Groq API key inside `app.py`
client = Groq(api_key="YOUR_GROQ_API_KEY")


4. Start the application
streamlit run app.py

---

## 💡 Example Questions
- What is Retrieval Augmented Generation?  
- Explain vector search  
- How do embeddings work?

---

