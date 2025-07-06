from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from InstructorEmbedding import INSTRUCTOR
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import gradio as gr

retriever_cache = None

groq_api_key = "your_groq_api_key_here"  # 🔐 Replace with your real Groq API key

def ask_question(file, user_question):
    global retriever_cache

    if file is None or user_question.strip() == "":
        return "❌ Please upload a file and enter a question."

    if retriever_cache is None:
        loader = PyPDFLoader(file.name) if file.name.endswith(".pdf") else TextLoader(file.name)
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
        docs = splitter.split_documents(documents)

        embed_model = HuggingFaceEmbeddings(
            model_name="intfloat/multilingual-e5-large",
            encode_kwargs={"normalize_embeddings": True}
        )

        vectorstore = FAISS.from_documents(docs, embed_model)
        retriever_cache = vectorstore.as_retriever()

    llm = ChatGroq(
        model="llama3-70b-8192",
        groq_api_key=groq_api_key
    )

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever_cache,
        return_source_documents=False
    )

    result = rag_chain.invoke(user_question)
    return f"📌 **Answer:**\n\n{result['result']}"

gr.Interface(
    fn=ask_question,
    inputs=[
        gr.File(label="📂 Upload your Business Document (.pdf or .txt)", type="filepath"),
        gr.Textbox(label="💬 Ask a question related to the document", placeholder="e.g., What are the key takeaways?")
    ],
    outputs=gr.Markdown(label="🧠 Answer"),
    title="📘 Business RAG Q&A Assistant",
    description=(
        "A smart assistant for business documents using Retrieval-Augmented Generation (RAG).\n\n"
        "Powered by:\n"
        "🔹 LLaMA3-70B via Groq\n"
        "🔹 multilingual-e5-large embeddings\n"
        "🔹 FAISS vector database"
    ),
    theme=gr.themes.Base(
        primary_hue="blue",
        secondary_hue="gray",
        font=["Inter", "sans-serif"]
    ),
    allow_flagging="never"
).launch(share=True)
