# 1. Use the FULL Python version (Includes all build tools)
FROM python:3.9

# 2. Set up the working directory
WORKDIR /app

# 3. Copy dependencies
COPY requirements.txt .

# 4. Upgrade pip and install libraries
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 5. Download the spaCy brain
RUN python -m spacy download en_core_web_sm

# 6. Copy the rest of the code
COPY . .

# 7. Launch
EXPOSE 7860
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]