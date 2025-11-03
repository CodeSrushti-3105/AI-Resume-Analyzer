🧠 AI Resume Analyzer

An AI-powered web app that analyzes resumes against job descriptions and calculates a Job Fit Score using NLP and Sentence Transformers.
It identifies matched and missing skills, helping candidates optimize their resumes for specific job roles.

🚀 Features

📄 Upload a resume (PDF or text)

📝 Paste a job description

⚡ Get a Job Fit Score instantly

🎯 View matched and missing skills

🧩 Built with Flask, HTML/CSS, and Python NLP models

🧰 Tech Stack
Component	Technology
Backend	Flask (Python)
NLP Model	SentenceTransformer (all-MiniLM-L6-v2)
Libraries	PyPDF2, scikit-learn, torch
Frontend	HTML, CSS (Jinja2 templates)

🛠️ Setup Instructions

1️⃣ Clone the Repository
git clone https://github.com/CodeSrushti-3105/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

2️⃣ Create a Virtual Environment

For Windows:

python -m venv venv
venv\Scripts\activate


For Mac/Linux:

python -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Flask App
python app.py

5️⃣ Open the App in Your Browser
http://127.0.0.1:5000/

💡 Example Output
Job Fit Score: 78.42%
✅ Matched Skills: Python, Flask, Docker, PostgreSQL
⚠️ Missing Skills: AWS, DevOps

🌟 Future Enhancements

Integration with LinkedIn for direct profile analysis

Resume optimization suggestions using AI

Support for multiple languages and job categories
