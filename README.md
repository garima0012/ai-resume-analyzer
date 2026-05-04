# 🧠 AI Resume Analyzer

> NLP-powered resume ↔ job description matcher with match scores, skill gap analysis, and actionable recruiter feedback.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)](https://streamlit.io)
[![spaCy](https://img.shields.io/badge/spaCy-3.7-09a3d5?logo=spacy)](https://spacy.io)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/ai-resume-analyzer/blob/main/AI_Resume_Analyzer.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📸 Demo

![App Screenshot](assets/demo.png)

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Resume Parsing** | Upload PDF/DOCX or paste text directly |
| 🎯 **Match Scoring** | TF-IDF cosine similarity + skill overlap scoring |
| 🔬 **NLP Entity Extraction** | Named entities via spaCy (ORG, GPE, DATE...) |
| 🛠️ **Skill Gap Analysis** | 80+ tech skills matched against job description |
| 📊 **Section Breakdown** | Skills · Relevance · Education · Experience scores |
| 💡 **Actionable Feedback** | Personalized tips for improving your resume |
| 🎓 **Education Detection** | Regex-based degree level detection |
| 💼 **Experience Detection** | Automatic years-of-experience extraction |

---

## 🚀 Quick Start

### Option 1 — Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# 3. Launch
streamlit run app.py
```

App opens at `http://localhost:8501` 🎉

---

### Option 2 — Run on Google Colab (no install needed)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/ai-resume-analyzer/blob/main/AI_Resume_Analyzer.ipynb)

1. Click the badge above
2. Run Cell 1 (installs dependencies)
3. Run Cell 2 (clones repo)
4. Add your free [ngrok token](https://ngrok.com) and run Cell 3
5. Open the generated public URL 🚀

---

## 🗂️ Project Structure

```
ai-resume-analyzer/
│
├── app.py                    # Streamlit UI
├── requirements.txt          # Dependencies
├── AI_Resume_Analyzer.ipynb  # Google Colab notebook
│
├── utils/
│   ├── __init__.py
│   ├── analyzer.py           # Core NLP engine (spaCy + NLTK + TF-IDF)
│   ├── parser.py             # PDF / DOCX text extraction
│   └── visualizer.py        # Plotly chart components
│
└── assets/
    └── demo.png              # Screenshot for README
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

### Scoring Weights

| Component | Method | Weight |
|---|---|---|
| Skills | Set intersection / JD skill count | 25% |
| Relevance | TF-IDF cosine similarity | 25% |
| Education | Regex degree detection | 25% |
| Experience | Regex years extraction | 25% |

---

## 🛠️ Tech Stack

- **[spaCy](https://spacy.io)** — Named Entity Recognition, tokenization
- **[NLTK](https://www.nltk.org)** — Stopword removal, text preprocessing
- **[scikit-learn](https://scikit-learn.org)** — TF-IDF vectorization, cosine similarity
- **[Streamlit](https://streamlit.io)** — Interactive web UI
- **[Plotly](https://plotly.com)** — Interactive charts
- **[pdfplumber](https://github.com/jsvine/pdfplumber)** — PDF text extraction
- **[python-docx](https://python-docx.readthedocs.io)** — DOCX parsing

---

## 📈 Sample Output

```
══════════════════════════════════════════════════
  OVERALL MATCH SCORE: 76%
══════════════════════════════════════════════════

📊 Section Scores:
  Skills       [████████░░] 80%
  Relevance    [███████░░░] 72%
  Education    [███████░░░] 70%
  Experience   [████████░░] 80%

✅ Matched Skills (8):
  docker, git, nltk, numpy, pytorch, python, spacy, tensorflow

❌ Missing Skills (3):
  kubernetes, bert, transformers

🎓 Education: Bachelor's
💼 Experience: Mid-level (3 yrs)
```

---

## 🤝 Contributing

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m 'Add your feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

MIT © [Your Name](https://github.com/YOUR_USERNAME)
