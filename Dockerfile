# 1. Use a lightweight Python setup
FROM python:3.9-slim

# 2. Set up the working directory
WORKDIR /app

# 3. Copy dependencies first (for faster builds)
COPY requirements.txt .

# 4. Install libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. CRITICAL: Download the spaCy brain (This fixes the common crash)
RUN python -m spacy download en_core_web_sm

# 6. Copy the rest of your app code
COPY . .

# 7. Open the port for Hugging Face
EXPOSE 7860

# 8. Launch the app
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]