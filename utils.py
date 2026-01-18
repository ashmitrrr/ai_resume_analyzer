import pdfplumber
import spacy
from sentence_transformers import SentenceTransformer, util

#NLP model (for keyword extraction)
nlp = spacy.load("en_core_web_sm")

#Transformer Model (for semantic understanding)
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(uploaded_file):
    """
    Robustly extracts text from a PDF file using pdfplumber.
    """
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
    return text

def extract_keywords(text):
    """
    Extracts potential skills/keywords using spaCy (NLP).
    It looks for Proper Nouns (PROPN) and Nouns to identify technical terms.
    """
    doc = nlp(text)

    keywords = [token.text.lower() for token in doc 
                if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and token.is_alpha]
    return set(keywords)

def get_match_score(resume_text, job_description):
    """
    Calculates the 'Semantic Match Score' using Transformers.
    This understands context (e.g., 'coding' matches 'programming').
    """
    #texts to Embeddings (Vector numbers)
    embeddings1 = model.encode(resume_text, convert_to_tensor=True)
    embeddings2 = model.encode(job_description, convert_to_tensor=True)
    
    # Cosine Similarity
    #raw score
    similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
    
    # convert to percentage
    score = similarity.item() * 100
    
    return round(score, 2)

def find_missing_skills(resume_text, job_description):
    """
    Identifies important keywords present in the JD but missing in the Resume.
    """
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    
    # difference
    missing = job_keywords - resume_keywords
    
    # only keep missing words that are kind of major (len > 3)
    # avoid suggesting random short words
    filtered_missing = [word for word in missing if len(word) > 3]
    
    return list(filtered_missing)