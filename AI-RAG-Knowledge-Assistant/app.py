import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from groq import Groq
import os

st.set_page_config(page_title="Endee RAG Assistant", layout="wide")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("💬 Chats")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.button("➕ New Chat"):
        st.session_state.messages = []

# ---------- MODELS ----------
model = SentenceTransformer("all-MiniLM-L6-v2")

import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

documents = [
    "Endee.io is a platform focused on vector search and AI infrastructure.",
    "Vector databases store embeddings that allow semantic similarity search.",
    "Retrieval Augmented Generation combines retrieval with language models.",
    "RAG improves accuracy by retrieving relevant context before generating answers."
]

doc_embeddings = model.encode(documents)

# ---------- CENTER WELCOME ----------
if len(st.session_state.messages) == 0:

    st.markdown(
        """
        <div style="text-align:center; margin-top:150px;">
            <h1>🤖 Endee Vector Search RAG Assistant</h1>
            <h3>How can I help you today?</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- DISPLAY CHAT ----------
for msg in st.session_state.messages:

    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])

    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])

# ---------- INPUT ----------
if prompt := st.chat_input("Ask a question..."):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # ---------- VECTOR SEARCH ----------
    query_embedding = model.encode([prompt])
    scores = np.dot(doc_embeddings, query_embedding.T).flatten()
    top_results = np.argsort(scores)[-3:][::-1]

    context = "\n".join([documents[i] for i in top_results])

    rag_prompt = f"""
    You are an AI assistant.

    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {prompt}

    Provide a clear explanation.
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": rag_prompt}
        ]
    )

    answer = completion.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )