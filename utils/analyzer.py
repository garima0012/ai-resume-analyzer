"""
analyzer.py – Core NLP analysis engine.

Uses spaCy for NER + tokenization, NLTK for preprocessing,
and scikit-learn TF-IDF + cosine similarity for scoring.
"""
from __future__ import annotations

import re
import string
from typing import Any

import nltk
import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── One-time downloads ─────────────────────────────────────────────────────────
for resource in ["stopwords", "punkt", "wordnet"]:
    try:
        nltk.data.find(f"corpora/{resource}")
    except LookupError:
        nltk.download(resource, quiet=True)

# ── spaCy model ────────────────────────────────────────────────────────────────
try:
    NLP = spacy.load("en_core_web_sm")
except OSError:
    import subprocess, sys
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], check=True)
    NLP = spacy.load("en_core_web_sm")

STOP_WORDS = set(stopwords.words("english"))

# ── Curated tech-skill vocabulary ─────────────────────────────────────────────
SKILL_VOCAB: set[str] = {
    # Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust",
    "kotlin", "swift", "ruby", "php", "scala", "r", "matlab", "bash",
    # Web
    "react", "angular", "vue", "nextjs", "nodejs", "django", "flask",
    "fastapi", "spring", "html", "css", "rest", "graphql", "grpc",
    # Data / ML / AI
    "pytorch", "tensorflow", "keras", "sklearn", "scikit-learn",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly", "huggingface",
    "llm", "nlp", "spacy", "nltk", "bert", "gpt", "transformers",
    "computer vision", "opencv", "yolo",
    # Cloud & DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "terraform",
    "ansible", "jenkins", "github actions", "ci/cd", "linux",
    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
    "cassandra", "bigquery", "snowflake",
    # Tools / Practices
    "git", "agile", "scrum", "jira", "figma", "tableau", "power bi",
    "excel", "spark", "kafka", "airflow", "mlflow",
}

# ── Education keywords ─────────────────────────────────────────────────────────
EDU_PATTERNS = {
    "PhD": r"\b(ph\.?d|doctor(ate)?)\b",
    "Master's": r"\b(m\.?s\.?|m\.?tech|master('s)?|mba)\b",
    "Bachelor's": r"\b(b\.?s\.?|b\.?tech|b\.?e\.?|bachelor('s)?|undergraduate|b\.?sc)\b",
    "Associate": r"\bassociate\b",
    "Diploma": r"\bdiploma\b",
}

# ── Experience regexes ─────────────────────────────────────────────────────────
EXP_RE = re.compile(r"(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s+)?(?:experience|exp)", re.I)


class ResumeAnalyzer:
    """Analyzes a resume against a job description using NLP techniques."""

    # ── Public entry point ─────────────────────────────────────────────────────
    def analyze(self, resume: str, jd: str) -> dict[str, Any]:
        resume_clean = self._preprocess(resume)
        jd_clean = self._preprocess(jd)

        resume_skills = self._extract_skills(resume)
        jd_skills = self._extract_skills(jd)

        matched = resume_skills & jd_skills
        missing = jd_skills - resume_skills

        tfidf_score = self._tfidf_similarity(resume_clean, jd_clean)
        skill_score = (len(matched) / max(len(jd_skills), 1)) * 100
        edu_match = self._detect_education(resume)
        exp_level = self._detect_experience(resume)

        section_scores = {
            "Skills": round(skill_score),
            "Relevance": round(tfidf_score * 100),
            "Education": self._edu_score(edu_match),
            "Experience": self._exp_score(exp_level),
        }
        overall = round(sum(section_scores.values()) / len(section_scores))

        entities = [(ent.text, ent.label_) for ent in NLP(resume[:5000]).ents
                    if ent.label_ in {"ORG", "GPE", "PERSON", "DATE", "PRODUCT"}]

        keywords = self._top_keywords(resume_clean, jd_clean)
        feedback = self._generate_feedback(matched, missing, edu_match, exp_level, overall)

        return {
            "overall_score": overall,
            "section_scores": section_scores,
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing),
            "matched_skills_count": len(matched),
            "missing_skills_count": len(missing),
            "total_jd_skills": max(len(jd_skills), 1),
            "education_match": edu_match,
            "experience_level": exp_level,
            "entities": entities[:15],
            "top_keywords": keywords,
            "feedback": feedback,
        }

    # ── NLP helpers ───────────────────────────────────────────────────────────
    def _preprocess(self, text: str) -> str:
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        tokens = [w for w in text.split() if w not in STOP_WORDS and len(w) > 1]
        return " ".join(tokens)

    def _extract_skills(self, text: str) -> set[str]:
        text_lower = text.lower()
        found: set[str] = set()
        for skill in SKILL_VOCAB:
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, text_lower):
                found.add(skill)
        return found

    def _tfidf_similarity(self, a: str, b: str) -> float:
        try:
            vec = TfidfVectorizer(ngram_range=(1, 2))
            tfidf = vec.fit_transform([a, b])
            return float(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0])
        except Exception:
            return 0.0

    def _detect_education(self, text: str) -> str:
        text_lower = text.lower()
        for degree, pattern in EDU_PATTERNS.items():
            if re.search(pattern, text_lower):
                return degree
        return "Not Detected"

    def _detect_experience(self, text: str) -> str:
        matches = EXP_RE.findall(text)
        if matches:
            years = max(int(y) for y in matches)
            if years >= 10:
                return f"Senior ({years}+ yrs)"
            elif years >= 4:
                return f"Mid-level ({years} yrs)"
            elif years >= 1:
                return f"Junior ({years} yrs)"
        return "Entry / Not Specified"

    def _top_keywords(self, resume: str, jd: str, n: int = 10) -> list[str]:
        try:
            vec = TfidfVectorizer(ngram_range=(1, 2), max_features=200)
            vec.fit([jd])
            scores = zip(vec.get_feature_names_out(), vec.transform([resume]).toarray()[0])
            ranked = sorted(scores, key=lambda x: x[1], reverse=True)
            return [w for w, s in ranked if s > 0][:n]
        except Exception:
            return []

    # ── Scoring helpers ───────────────────────────────────────────────────────
    def _edu_score(self, edu: str) -> int:
        return {"PhD": 100, "Master's": 85, "Bachelor's": 70,
                "Associate": 55, "Diploma": 45}.get(edu, 30)

    def _exp_score(self, exp: str) -> int:
        if "Senior" in exp:   return 95
        if "Mid" in exp:      return 70
        if "Junior" in exp:   return 45
        return 30

    # ── Feedback generation ───────────────────────────────────────────────────
    def _generate_feedback(self, matched, missing, edu, exp, score) -> list[str]:
        fb = []
        if score >= 70:
            fb.append("🟢 Strong profile! Your resume aligns well with this job description.")
        elif score >= 40:
            fb.append("🟡 Moderate match. A few targeted improvements could make you competitive.")
        else:
            fb.append("🔴 Low match. Consider tailoring your resume specifically for this role.")

        if missing:
            top_missing = list(missing)[:5]
            fb.append(f"❌ Missing key skills: **{', '.join(top_missing)}**. Add these if applicable.")

        if len(matched) >= 5:
            fb.append(f"✅ Great skill coverage — {len(matched)} job-required skills detected in your resume.")

        if edu == "Not Detected":
            fb.append("📚 No clear education section detected. Add your degree/certification explicitly.")
        else:
            fb.append(f"🎓 Education detected: **{edu}**.")

        if "Entry" in exp or "Not" in exp:
            fb.append("💼 No explicit years of experience found. Consider stating '3+ years of experience in...'")
        else:
            fb.append(f"💼 Experience level detected: **{exp}**.")

        fb.append("📝 Tip: Mirror keywords from the job description naturally throughout your resume.")
        fb.append("📊 Tip: Quantify your achievements (e.g., 'Improved performance by 35%') for impact.")
        return fb
