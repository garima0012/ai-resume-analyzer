# 🧠 AI Resume Analyzer

> NLP-powered resume ↔ job description matcher with match scores, skill gap analysis, and actionable feedback.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)](https://streamlit.io)
[![spaCy](https://img.shields.io/badge/spaCy-3.7-09a3d5)](https://spacy.io)
[![NLTK](https://img.shields.io/badge/NLTK-3.8-green)](https://www.nltk.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Live Demo

👉 **[Click here to try the app](YOUR_STREAMLIT_URL)**

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

## 🗂️ Project Structure---

## 🔬 How It Works---

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
git clone https://github.com/garima0012/ai-resume-analyzer.git
cd ai-resume-analyzer
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Run on Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/garima0012/ai-resume-analyzer/blob/main/AI_Resume_Analyzer.ipynb)

---

## 📄 License

MIT © [Garima](https://github.com/garima0012)
