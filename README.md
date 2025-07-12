# 🧠 Basic RAG-LLM Playground

This repository provides a simple, modular implementation of a **Retrieval-Augmented Generation (RAG)** pipeline using open-source language models. It allows users to convert documents into searchable knowledge, experiment with local LLMs, and interact with them via a command-line interface.

## ✨ Features

- 🔽 **Download & Load Open-Source LLMs Locally**  
Automatically fetch and run open-source language models on your machine.

- 📄 **PDF to Text Conversion**  
Extracts raw text from PDF files for downstream processing.

- ✂️ **Text Chunking & Embedding**  
Splits text into manageable chunks and embeds them into a vector database.

- 🧠 **Vector Search with RAG**  
Retrieves the most relevant chunks based on a user query and builds a prompt for the LM.

- 💬 **CLI-Based Interaction**  
Ask questions via the command line and receive context-aware answers from your local model.

## 📁 Project Structure

```
basic-rag-llm/
├── pdf_docs/                   # Source PDF files for RAG use
├── .gitignore                  # These aren't the files you're looking for
├── README.md                   # You're here!
├── requirements.txt            # Python dependencies
├── step1_save_models.py        # Download local language models
├── step2_pdf_to_txt.py         # Convert PDF files to .txt files
├── step3_create_vector_db.py   # Chunk the text, vectorize it, store it
├── step4_cli_rag_chatbot.py    # Core RAG logic (retrieval and prompting)
```

## 🚀 Getting Started

### 1.	Clone the repository
```shell
git clone https://github.com/dsiwg/basic-rag-llm.git
cd basic-rag-llm
```

### 2.  Install dependencies
```shell
pip install -r requirements.txt
```

### 3.  Download local embedding and text generation models
```shell
python step1_save_models.py 
```

### 4.  Convert PDFs to Text
```shell
python step2_pdf_to_txt.py 
```

### 5.  Chunk & Embed Text
```shell
python step3_create_vector_db.py
```

### 5.  Ask Questions via CLI
```shell
python step4_cli_rag_chatbot.py
```

## 🛠️ Tech Stack
-   Python
-   [SentenceTransformers](https://huggingface.co/sentence-transformers) for embedding model
-   [HuggingFace_Hub](https://github.com/huggingface/huggingface_hub) to download text gener model
-   [Llama-cpp-python](https://github.com/abetlen/llama-cpp-python) to interact with text gen model
-   [PyMuPDF](https://github.com/pymupdf/PyMuPDF) for PDF parsing

## 📌 Notes
-   This project is designed for educational and experimental purposes.
-   Performance and accuracy will depend on the model and hardware used.
-   You can easily swap components (e.g., vector DB, model) to suit your needs.

## 🤘 Thanks
This code was made possible thanks to support from [Ben Listyg @ INPO](https://www.linkedin.com/in/benlistyg/).

## 📚 Resources
-   [Hugging Face Model Hub](https://huggingface.co/models)
-   [How LLMs Work](https://ig.ft.com/generative-ai/)
-   [Code a simple RAG from scratch](https://huggingface.co/blog/ngxson/make-your-own-rag)
-   Nuclear Power Related AI Research
    -   [Technology Deployment Plan for Emerging Technologies in Nuclear Power Plants](https://lwrs.inl.gov/content/uploads/11/2025/03/INLRPT-24-80012-Technology-Deployment-Plan-for-Emerging-Technologies-in-Nuclear-Power-Plants.pdf)
    -   [Scalable Methods to Automate Manual Work Management Activities Using Artificial Intelligence](https://lwrs.inl.gov/content/uploads/11/2024/09/ScalableMethodsAutomateManualWork.pdf)
    -   [Explainable Artificial Intelligence Technology for Predictive Maintenance](https://lwrs.inl.gov/content/uploads/11/2024/03/ExplainableArtificialIntelligenceTechnology.pdf)
    -   [Considerations for Developing Artificial Intelligence Systems in Nuclear Applications](https://www.nrc.gov/docs/ML2424/ML24241A252.pdf)
    -   [Exploring Advanced Computational Tools and Techniques with Artificial Intelligence and Machine Learning in Operating Nuclear Plants](https://www.nrc.gov/docs/ML2204/ML22042A662.pdf)


## 📬 Contact
For questions, suggestions, or collaboration inquiries, feel free to reach out:

[David A. Sluder](https://www.linkedin.com/in/david-sluder/)  
Senior Program Manager, Data Science  
Institute of Nuclear Power Operations  
📍 Atlanta, GA  
✉️ [sluderda@inpo.org](mailto:sluderda@inpo.org)

## 📄 License
This project is licensed under the MIT License.