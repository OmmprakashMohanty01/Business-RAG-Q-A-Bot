# 📘 Business RAG Q&A Assistant

A smart assistant for business documents using Retrieval-Augmented Generation (RAG).  
Built with **LLaMA3 via Groq**, **multilingual-e5-large embeddings**, and **FAISS vector DB**.

---

## 🚀 Features

- Upload `.pdf` or `.txt` business documents
- Ask natural language questions about the document content
- Instant answers using RAG pipeline
- Local FAISS index for fast retrieval
- Multilingual support via `intfloat/multilingual-e5-large` embeddings
- Powered by LLaMA3 hosted on Groq

---

## 📁 Project Structure

business-rag-qa-bot/
├── app.py # Main Gradio application
├── requirements.txt # All required Python dependencies
├── README.md # This documentation
├── task2.pdf # Optimization techniques report (Task 2)
├── task3.pdf # Dataset preparation report (Task 3)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/OmmprakashMohanty01/Business-RAG-Q-A-Bot.git
cd Business-RAG-Q-A-Bot
```
---

## 2. Create a Virtual Environment (Recommended)
``` bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```
--- 

### 3. Install Dependencies
``` bash 
pip install -r requirements.txt
```
--- 

### 4. Add Your Groq API Key
Open app.py and replace with your actual API key :
``` bash 
groq_api_key = "your_groq_api_key_here"
```
---
### 5. Run the Application
``` bash
python app.py
```
After launching, access the app using the local URL (http://127.0.0.1:7860) or Gradio public link in your browser.

---
### 💬 Example Questions to Ask
What are the key takeaways from this financial report?

Who are the stakeholders mentioned?

Summarize the executive summary section.

What does the document say about market trends?

---
### 📜 License
This project is licensed under the MIT License.

---

### 🌐 Powered By
Groq LLaMA3 API

HuggingFace Embeddings

Gradio UI

LangChain Framework

---
## 👤 Author

**Ommprakash Mohanty**  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/ommprakash-mohanty-366b73278)

Feel free to connect or reach out for collaboration!

---