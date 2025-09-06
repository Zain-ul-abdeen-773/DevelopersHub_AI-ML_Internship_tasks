# app_streamlit.py
import streamlit as st
from pathlib import Path
import json
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any

# --- HuggingFace LLM Wrapper for LangChain ---
class HuggingFaceLLMWrapper(LLM):
    def __init__(self, pipeline):
        self.pipeline = pipeline
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"pipeline": str(self.pipeline)}
    @property
    def _llm_type(self) -> str:
        return "huggingface-flan-t5"
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        out = self.pipeline(prompt, max_length=256, do_sample=False)
        return out[0]["generated_text"]

# --- UI Setup ---
st.set_page_config(page_title="Context-Aware RAG Chatbot", layout="wide")
st.title("🤖 Context-Aware Chatbot (RAG + LangChain)")

# --- Load manifest ---
manifest_path = Path("chroma_manifest.json")
if not manifest_path.exists():
    st.error("❌ chroma_manifest.json not found. Run the notebook first to create DB.")
    st.stop()

manifest = json.loads(manifest_path.read_text())

# --- Init embeddings + vectorstore ---
emb = HuggingFaceEmbeddings(model_name=manifest["embedding_model"], model_kwargs={"device": "cpu"})
vectordb = Chroma(persist_directory=manifest["persist_dir"], embedding_function=emb, collection_name=manifest["collection"])

# --- Init generator ---
gen_model = manifest["generator"]
tokenizer = AutoTokenizer.from_pretrained(gen_model)
model = AutoModelForSeq2SeqLM.from_pretrained(gen_model)
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)
hf_llm = HuggingFaceLLMWrapper(generator)

# --- Build RAG Chain ---
retriever = vectordb.as_retriever(search_kwargs={"k": 5})
rag_chain = ConversationalRetrievalChain.from_llm(hf_llm, retriever, return_source_documents=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat UI ---
user_input = st.text_input("💬 Ask something about your documents:", key="input")
if st.button("Send") and user_input:
    result = rag_chain({"question": user_input, "chat_history": st.session_state.chat_history})
    answer = result["answer"]
    sources = result.get("source_documents", [])
    st.session_state.chat_history.append((user_input, answer))

    st.markdown("### 🧠 Answer")
    st.write(answer)

    if sources:
        st.markdown("### 📚 Sources")
        for s in sources[:3]:
            st.json(s.metadata)

# --- Display conversation history ---
if st.session_state.chat_history:
    st.markdown("### 🗂️ Conversation History")
    for i, (q, a) in enumerate(st.session_state.chat_history):
        st.write(f"**Q{i+1}:** {q}")
        st.write(f"**A{i+1}:** {a}")
        st.write("---")
