import streamlit as st
import utils
import time

st.set_page_config(
    page_title="AI RESUME ANALYZER",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# css
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* 1. GLOBAL DARK THEME */
    .stApp {
        background-color: #0e1117;
    }
    
    html, body, [class*="css"], h1, h2, h3, div, span, p {
        font-family: 'Inter', sans-serif;
        color: #e2e8f0 !important;
    }
    
    p[style*="color: #6b7280"] {
         color: #94a3b8 !important;
    }
    
    /* 2. CUSTOM CARDS */
    .st-card {
        background-color: #1e293b;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        border: 1px solid #334155;
        margin-bottom: 20px;
        transition: transform 0.2s ease;
    }
    
    .st-card:hover {
        transform: translateY(-5px);
        border-color: #6366f1;
    }

    /* 3. METRICS */
    .score-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    
    .score-value {
        font-size: 4rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #6366f1, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 4. TAGS */
    .skill-tag {
        display: inline-block;
        background-color: rgba(99, 102, 241, 0.1);
        color: #818cf8 !important;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        margin: 4px;
        border: 1px solid #4f46e5;
    }
    
    .skill-tag.missing {
        background-color: rgba(239, 68, 68, 0.1);
        color: #f87171 !important;
        border: 1px solid #ef4444;
    }

    /* 5. VISIBILITY & BUTTONS */
    #MainMenu, footer, header {visibility: hidden;}
    
    .stButton > button {
        background: linear-gradient(90deg, #4f46e5 0%, #06b6d4 100%);
        color: white !important;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        border-radius: 8px;
        width: 100%;
        transition: opacity 0.3s;
    }
    .stButton > button:hover {
        opacity: 0.9;
        box-shadow: 0 0 15px rgba(79, 70, 229, 0.5);
    }
    
    /* 6. INPUT FIXES */
    .stTextInput input, .stTextArea textarea {
        background-color: #1e293b !important;
        color: #818cf8 !important;
        border-color: #475569 !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #6366f1 !important;
    }
    
    /* Uploader Visibility Fix */
    [data-testid="stFileUploader"] > div > div {
        background-color: #1e293b !important;
        border-color: #475569 !important;
    }
    [data-testid="stFileUploader"] div, 
    [data-testid="stFileUploader"] span, 
    [data-testid="stFileUploader"] svg {
        color: #818cf8 !important;
        fill: #818cf8 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; padding: 50px 0;">
        <h1 style="font-size: 3.5rem; margin-bottom: 10px; background: -webkit-linear-gradient(45deg, #ffffff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
             AI Resume Analyzer
        </h1>
        <p style="color: #94a3b8 !important; font-size: 1.2rem; max-width: 600px; margin: 0 auto;">
            Unlock the power of <span style="color: #818cf8;">Neural Networks</span> to optimize your CV.
        </p>
    </div>
""", unsafe_allow_html=True)



col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 1. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf", label_visibility="collapsed")

with col2:
    st.markdown("### 2. Job Description")
    job_description = st.text_area("Paste JD", height=150, placeholder="Paste job description...", label_visibility="collapsed")

btn_col1, btn_col2 = st.columns([1, 1], gap="large")

with btn_col1:
    st.markdown("<br>", unsafe_allow_html=True) # Little breathing room
    analyze_btn = st.button("🚀 Analyze Compatibility Now")

if analyze_btn:
    if uploaded_file and job_description:
        with st.spinner("Initializing Transformer Models..."):
            time.sleep(1)
            try:
                resume_text = utils.extract_text_from_pdf(uploaded_file)
                if not resume_text:
                    st.error(" Error: Could not read text from this PDF.")
                else:
                    match_score = utils.get_match_score(resume_text, job_description)
                    missing_skills = utils.find_missing_skills(resume_text, job_description)
                    
                    st.markdown("---")
                    
                    # SCORE CARD
                    st.markdown(f"""
                        <div class="st-card score-container">
                            <h3 style="color: #94a3b8 !important; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1.5px;">Semantic Match Score</h3>
                            <div class="score-value">{match_score}%</div>
                            <p style="color: #94a3b8 !important; margin-top: 10px;">
                                {"✅ Highly Compatible" if match_score >= 70 else "⚠️ Optimization Required"}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)

                    # DETAILS GRID
                    c1, c2 = st.columns(2, gap="large")
                    
                    with c1:
                        html_tags = ""
                        if missing_skills:
                            for skill in missing_skills:
                                html_tags += f'<span class="skill-tag missing">❌ {skill.title()}</span>'
                        else:
                            html_tags = '<span class="skill-tag">✅ No gaps found!</span>'
                            
                        st.markdown(f"""
                            <div class="st-card">
                                <h3>📉 Missing Keywords</h3>
                                <p style="color: #94a3b8 !important; font-size: 0.9rem; margin-bottom: 15px;">
                                    High-value terms missing from your resume:
                                </p>
                                <div>{html_tags}</div>
                            </div>
                        """, unsafe_allow_html=True)

                    with c2:
                        if match_score < 60:
                            advice = "Your syntax is different. Mirror the exact verbs used in the JD."
                        elif match_score < 80:
                            advice = "Good foundation! Add the missing keywords to your Skills section."
                        else:
                            advice = "Excellent match! Focus on quantifying your impact."

                        st.markdown(f"""
                            <div class="st-card">
                                <h3>💡 Strategic Advice</h3>
                                <p style="font-size: 1.1rem; line-height: 1.6; color: #e2e8f0 !important;">
                                    "{advice}"
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with st.expander("View Processed Text"):
                        st.text(resume_text[:2000] + "...")

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("⚠️ Please upload a resume and paste a job description.")