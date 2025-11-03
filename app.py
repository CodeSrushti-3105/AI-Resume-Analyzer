from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer, util
import PyPDF2
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

# -------- Extract text from uploaded PDF --------
def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# -------- Extract meaningful keywords --------
def extract_keywords(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s+]', '', text)
    words = [w for w in text.split() if w not in ENGLISH_STOP_WORDS and len(w) > 2]
    return set(words)

# -------- Home page --------
@app.route('/')
def index():
    return render_template('index.html')

# -------- Analyze route --------
@app.route('/analyze', methods=['POST'])
def analyze():
    resume_text = ""

    # --- 1️⃣ Get resume text ---
    if 'resume_pdf' in request.files and request.files['resume_pdf'].filename != '':
        pdf_file = request.files['resume_pdf']
        resume_text = extract_text_from_pdf(pdf_file)
    elif 'resume_text' in request.form and request.form['resume_text'].strip() != '':
        resume_text = request.form['resume_text']
    else:
        return render_template('index.html', error="⚠️ Please upload or paste a resume first!")

    # --- 2️⃣ Get job description ---
    jd_text = request.form['jd']
    if not jd_text.strip():
        return render_template('index.html', error="⚠️ Please enter a Job Description!")

    # --- 3️⃣ Calculate semantic similarity score ---
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    fit_score = round(float(score.item()) * 100, 2)

    # --- 4️⃣ Extract and compare skills ---
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched_skills = sorted(list(resume_keywords & jd_keywords))
    missing_skills = sorted(list(jd_keywords - resume_keywords))

    return render_template(
        'index.html',
        fit_score=fit_score,
        matched=matched_skills,
        missing=missing_skills
    )

if __name__ == '__main__':
    app.run(debug=True)
