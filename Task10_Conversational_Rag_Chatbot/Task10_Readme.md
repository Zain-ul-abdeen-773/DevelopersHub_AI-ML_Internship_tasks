# 🗨️ Task 10: Context-Aware Chatbot using LangChain + RAG

This project is part of the **DevelopersHub AI/ML Internship**.  
It builds a **context-aware chatbot** using **Retrieval-Augmented Generation (RAG)** with **LangChain** and **HuggingFace models**. The chatbot can answer multi-turn questions based on uploaded documents such as PDFs or text files.

---

## 🎯 Objective

- Build a chatbot that can answer questions using **document context**  
- Implement **RAG pipeline** with embeddings + vector database + generator model  
- Support **multi-turn conversation** (chat history aware)  
- Deploy as an **interactive Streamlit app**  

---

## 💡 Key Features

- Supports `.pdf`, `.txt`, `.md` files for knowledge ingestion  
- Automatic text chunking and embedding with **MiniLM sentence-transformer**  
- Vector database built with **Chroma** for retrieval  
- Generation with **Flan-T5** (local HuggingFace model, no API needed)  
- Multi-turn conversation memory (chat history)  
- Streamlit UI with conversation history and source inspection  

---

## 📋 Example Use Cases

- Ask questions about your **internship tasks** (upload the PDF)  
- Build a chatbot for **course notes or research papers**  
- Use it as a **context-aware assistant** for project documentation  

---

## ⚙️ How to Run (Step-by-Step)

### Step 1: Clone the Repo  
Clone the GitHub repository and navigate to the project folder.

### Step 2: Install Dependencies  
Install the required Python libraries:  
\`pip install streamlit langchain chromadb sentence-transformers transformers torch\`

### Step 3: Add Documents  
Place your `.pdf` or `.txt` files inside the `docs/` folder.  
Example:  

---


### Step 4: Build Vector Database  
Run the notebook `RAG_Chatbot_Notebook.ipynb` to:  
- Load and split documents  
- Embed chunks using MiniLM  
- Store embeddings in Chroma (`chroma_db/`)  
- Generate `chroma_manifest.json`

### Step 5: Launch Streamlit App  
\`streamlit run app_streamlit.py\`  

Open the app in your browser at 👉 http://localhost:8501

---

## 📉 Bonus Visualizations

- Inspect retrieved chunks for a query  
- Multi-turn evaluation with structured prompts  
- View embedding space statistics (optional extensions)  

---

## 👨‍💻 Author

**Zain ul Abdeen**  
Intern ID: DHC-1204  
BS in Artificial Intelligence  
GitHub: [Zain-ul-abdeen-773](https://github.com/Zain-ul-abdeen-773)  
Portfolio: [zain-ul-abdeen-773.netlify.app](https://zain-ul-abdeen-773.netlify.app/)  
LinkedIn: [linkedin.com/in/zain-ul-abdeen-48aa72318](http://www.linkedin.com/in/zain-ul-abdeen-48aa72318)

---

## 📜 License

This project is open for educational use under the MIT License.

---

## ⭐️ Feedback

If this notebook and chatbot helped you or inspired you, please ⭐️ the repository and share your feedback.  
Your support helps the open-source and AI learning community grow!
