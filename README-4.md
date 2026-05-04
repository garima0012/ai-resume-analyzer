# 🧠 AI Resume Analyzer

> NLP-powered resume ↔ job description matcher with match scores, skill gap analysis, and actionable feedback for recruiters and candidates.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)](https://streamlit.io)
[![spaCy](https://img.shields.io/badge/spaCy-3.7-09a3d5)](https://spacy.io)
[![NLTK](https://img.shields.io/badge/NLTK-3.8-green)](https://www.nltk.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Live Demo

👉 **[Click here to try the app](YOUR_STREAMLIT_URL)**

---

## 📸 Screenshot

![AI Resume Analyzer Screenshot](assets/demo.png)

---

## ✨ Features

- 📄 **Resume Parsing** — Upload PDF/DOCX or paste text directly
- 🎯 **Match Scoring** — TF-IDF cosine similarity + skill overlap scoring
- 🔬 **NLP Entity Extraction** — Named entities via spaCy (ORG, GPE, DATE...)
- 🛠️ **Skill Gap Analysis** — 80+ tech skills matched against job description
- 📊 **Section Breakdown** — Skills · Relevance · Education · Experience scores
- 💡 **Actionable Feedback** — Personalized tips for improving your resume
- 🎓 **Education Detection** — Regex-based degree level detection
- 💼 **Experience Detection** — Automatic years-of-experience extraction

---

## 🗂️ Project Structure

```
ai-resume-analyzer/
│
├── app.py                    # Streamlit UI
├── requirements.txt          # All dependencies
├── AI_Resume_Analyzer.ipynb  # Google Colab notebook
│
├── utils/
│   ├── analyzer.py           # Core NLP engine (spaCy + NLTK + TF-IDF)
│   ├── parser.py             # PDF / DOCX text extraction
│   └── visualizer.py        # Plotly chart components
│
└── assets/
    └── demo.png              # App screenshot
```

---

## 🔬 How It Works

```
Resume Text ──┐
              ├──► Text Preprocessing (NLTK stopwords, punctuation removal)
JD Text ──────┘
                         │
              ┌──────────▼──────────┐
              │   spaCy NLP Engine  │  ← Named Entity Recognition
              └──────────┬──────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
    Skill Matcher   TF-IDF Score   Regex Patterns
   (80+ tech terms) (cosine sim.)  (edu, exp, years)
          │              │              │
          └──────────────┼──────────────┘
                         ▼
               Weighted Overall Score
                         │
                         ▼
              Actionable Feedback Report
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| spaCy | Named Entity Recognition, tokenization |
| NLTK | Stopword removal, text preprocessing |
| scikit-learn | TF-IDF vectorization, cosine similarity |
| Streamlit | Interactive web UI |
| Plotly | Interactive charts |
| pdfplumber | PDF text extraction |
| python-docx | DOCX parsing |

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/garima0012/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch
streamlit run app.py
```

App opens at → `http://localhost:8501`

---

## ☁️ Run on Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/garima0012/ai-resume-analyzer/blob/main/AI_Resume_Analyzer.ipynb)

1. Click the badge above
2. Run Cell 1 — installs all packages
3. Run Cell 2 — clones repo
4. Add your free [ngrok token](https://ngrok.com) → Run Cell 3
5. Open the generated public URL 🚀

---

## 📄 License

MIT © [Garima](https://github.com/garima0012)
