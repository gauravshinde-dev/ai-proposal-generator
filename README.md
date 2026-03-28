📌 Overview
Resume Matching System is a recruiter-facing web tool that automates the resume screening process. Instead of manually reading through dozens of resumes, recruiters upload a job description and a set of resumes — the system ranks candidates by relevance score automatically.
Built as a final-year engineering project at MIT Academy of Engineering, Pune (2025), under the mentorship of Mrs. Shubhangi Kale.

✨ Key Features

🔍 NLP-based matching — TF-IDF vectorization + cosine similarity scoring
📂 Resume parsing pipeline — extracts text from PDF resumes using PyPDF2
🏆 Automated candidate ranking — sorts applicants by relevance score
🗝️ Keyword extraction — identifies matching and missing keywords per resume
🗄️ Database integration — stores results for later retrieval and comparison
📊 Recruiter dashboard — clean web UI built with Flask for non-technical users


📊 Results & Impact

Achieved ~72% matching accuracy on NLP-based resume-to-JD similarity scoring
Reduced manual resume screening effort by ~30%, enabling faster hiring decisions
Tested on real resume datasets with multi-keyword extraction and ranking
Full pipeline from PDF upload → text extraction → scoring → ranked output


🏗️ Architecture
Recruiter uploads Job Description + Resumes (PDF)
              ↓
         Flask Web App (main controller)
              ↓
      PyPDF2 → Text Extraction from PDFs
              ↓
      NLTK → Text Preprocessing & Cleaning
              ↓
   Scikit-learn → TF-IDF Vectorization
              ↓
      Cosine Similarity Scoring per Resume
              ↓
      Ranked Candidate List + Keyword Report
              ↓
       Results stored in Database
              ↓
      Recruiter Dashboard (Flask UI)

🛠️ Tech Stack
LayerTechnologyBackendPython, FlaskNLP & MLNLTK, Scikit-learn, TF-IDF, Cosine SimilarityPDF ParsingPyPDF2DatabaseSQL (results storage)FrontendHTML, CSS (Flask templates)Dev ToolsVS Code, Git

🚀 Getting Started
Prerequisites
bashpip install flask nltk scikit-learn pypdf2
Also download required NLTK data:
pythonimport nltk
nltk.download('stopwords')
nltk.download('punkt')
Setup & Run

Clone the repository

bashgit clone https://github.com/YOUR-USERNAME/resume-matching-system.git
cd resume-matching-system

Run the Flask app

bashpython app.py

Open your browser at:

http://localhost:5000

Upload a job description and one or more resumes (PDF format) and get ranked results instantly.


📁 Project Structure
resume-matching-system/
│
├── app.py                  # Flask app — routes & controller
├── matcher.py              # NLP pipeline — TF-IDF & cosine similarity
├── parser.py               # PDF text extraction via PyPDF2
├── database.py             # Result storage & retrieval
├── templates/
│   ├── index.html          # Upload page
│   └── results.html        # Ranked candidate dashboard
├── static/                 # CSS & assets
└── README.md

🖥️ How It Works

Upload — Recruiter pastes/uploads a Job Description and uploads resume PDFs
Parse — PyPDF2 extracts raw text from each resume
Preprocess — NLTK removes stopwords, tokenizes, and normalizes text
Vectorize — TF-IDF converts JD and resumes into numerical vectors
Score — Cosine similarity measures how close each resume is to the JD
Rank — Candidates are sorted from highest to lowest match score
Report — Dashboard shows scores, matched keywords, and missing keywords


👥 Team
Built by a team of 4 — MIT Academy of Engineering, Pune
Duration: March 2025 – May 2025

🔮 Future Roadmap

 Support for DOCX resume uploads
 BERT/Sentence-Transformer based semantic matching (beyond keyword overlap)
 Email shortlisting integration
 Multi-JD batch processing
 Admin login & session management
 Export results as Excel/CSV report


📬 Contact
Gaurav Shinde
📧 gaurav.shinde9401@gmail.com
🔗 https://www.linkedin.com/in/gaurav-shinde-3a3564338
