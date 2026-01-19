---
title: AI Resume Analyzer
emoji: 🤖
colorFrom: gray
colorTo: blue
sdk: docker
pinned: false
app_port: 7860
license: apache-2.0
---

# AI Resume Analyzer

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Open%20in%20Spaces-blue.svg)](https://huggingface.co/spaces/ashmitrrr/ai-resume-analyzer)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)

**Formulated a solution** to evaluate semantic compatibility between professional resumes and job descriptions using Deep Learning. This tool goes beyond simple keyword matching by utilizing **SBERT (Sentence-BERT)** to understand the context and nuance of candidate profiles.

---

## Key Features

* **Semantic Vector Analysis:** Utilizes `sentence-transformers` to generate high-dimensional embeddings for resumes and JDs, calculating cosine similarity scores that reflect true contextual match.
* **Intelligent Gap Analysis:** **Validates** candidate qualifications against job specifications to identify missing hard skills and keywords.
* **Privacy-First Architecture:** Designed with strict data privacy specifications—all processing occurs in-memory. No documents are stored or persisted after analysis.
* **Containerized Deployment:** Fully Dockerized application ensuring consistent performance across development and production environments.

## Technical Architecture

* **Core Engine:** Python 3.9
* **NLP Models:**
    * `sentence-transformers` (all-MiniLM-L6-v2) for semantic embeddings.
    * `spaCy` (en_core_web_sm) for entity recognition and keyword extraction.
* **Frontend:** Streamlit
* **Infrastructure:** Docker (Debian-based Python 3.9 image)

## Local Installation

To run this application in your local environment for development or testing:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ashmitrrr/Resume_Analyzer.git](https://github.com/ashmitrrr/Resume_Analyzer.git)
    cd Resume_Analyzer
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

4.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

## Docker Build

To validate the containerized components locally:

```bash
# Build the image
docker build -t resume-architect .

# Run the container
docker run -p 7860:7860 resume-architect

License
Distributed under the Apache 2.0 License. See LICENSE for more information.

Developed by Ashmit Raina