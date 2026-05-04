import streamlit as st
import time
from utils.parser import extract_text_from_pdf, extract_text_from_docx
from utils.analyzer import ResumeAnalyzer
from utils.visualizer import (
    render_score_gauge,
    render_skill_match_chart,
    render_section_scores,
)

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 { font-family: 'Space Mono', monospace; }

.main { background: #0d0d0d; }
.stApp { background: linear-gradient(135deg, #0d0d0d 0%, #111827 100%); }

.score-card {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    border: 1px solid #00f5a0;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 0 30px rgba(0,245,160,0.1);
}
.score-number {
    font-family: 'Space Mono', monospace;
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(90deg, #00f5a0, #00d9f5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.skill-tag {
    display: inline-block;
    background: rgba(0,245,160,0.15);
    color: #00f5a0;
    border: 1px solid rgba(0,245,160,0.3);
    border-radius: 20px;
    padding: 4px 14px;
    margin: 4px;
    font-size: 0.82rem;
    font-family: 'Space Mono', monospace;
}
.missing-tag {
    background: rgba(255,75,75,0.15);
    color: #ff4b4b;
    border-color: rgba(255,75,75,0.3);
}
.section-header {
    font-family: 'Space Mono', monospace;
    color: #00f5a0;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.feedback-box {
    background: rgba(255,255,255,0.03);
    border-left: 3px solid #00f5a0;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
    color: #ccc;
    font-size: 0.92rem;
}
.feedback-box.warning { border-left-color: #ffb347; }
.feedback-box.error   { border-left-color: #ff4b4b; }
</style>
""",
    unsafe_allow_html=True,
)

# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🧠 AI Resume Analyzer")
    st.markdown("---")
    st.markdown("**How it works:**")
    st.markdown(
        "1. Paste or upload your **Resume**\n"
        "2. Paste the **Job Description**\n"
        "3. Hit **Analyze** and get instant feedback"
    )
    st.markdown("---")
    st.markdown("**Built with:**")
    st.markdown("🐍 Python · spaCy · NLTK\nStreamlit · scikit-learn")
    st.markdown("---")
    st.caption("v1.0 · Made for recruiters & candidates")

# ─── Header ────────────────────────────────────────────────────────────────────
st.markdown("# 🧠 AI Resume Analyzer")
st.markdown(
    "<p style='color:#888; font-size:1rem;'>NLP-powered resume ↔ job description matcher with actionable feedback</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ─── Input Section ─────────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<p class="section-header">📄 Resume Input</p>', unsafe_allow_html=True)
    resume_tab1, resume_tab2 = st.tabs(["📝 Paste Text", "📁 Upload File"])
    with resume_tab1:
        resume_text_input = st.text_area(
            "Paste your resume here",
            height=300,
            placeholder="Paste your resume content...",
            label_visibility="collapsed",
        )
    with resume_tab2:
        uploaded_file = st.file_uploader(
            "Upload Resume", type=["pdf", "docx"], label_visibility="collapsed"
        )
        if uploaded_file:
            if uploaded_file.name.endswith(".pdf"):
                resume_text_input = extract_text_from_pdf(uploaded_file)
            else:
                resume_text_input = extract_text_from_docx(uploaded_file)
            st.success(f"✅ Loaded: `{uploaded_file.name}`")

with col2:
    st.markdown('<p class="section-header">💼 Job Description</p>', unsafe_allow_html=True)
    jd_text = st.text_area(
        "Paste the job description here",
        height=300,
        placeholder="Paste the job description...",
        label_visibility="collapsed",
    )

st.markdown("---")

# ─── Analyze Button ────────────────────────────────────────────────────────────
_, btn_col, _ = st.columns([2, 1, 2])
with btn_col:
    analyze_clicked = st.button("⚡ Analyze Resume", use_container_width=True, type="primary")

# ─── Results ───────────────────────────────────────────────────────────────────
if analyze_clicked:
    resume_text = resume_text_input if resume_text_input else ""
    if not resume_text.strip() or not jd_text.strip():
        st.warning("⚠️ Please provide both a resume and a job description.")
        st.stop()

    with st.spinner("🔍 Analyzing with NLP models..."):
        time.sleep(0.5)
        analyzer = ResumeAnalyzer()
        result = analyzer.analyze(resume_text, jd_text)

    st.markdown("---")
    st.markdown("## 📊 Analysis Results")

    # ── Top KPI Row ────────────────────────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    score = result["overall_score"]

    color = "#00f5a0" if score >= 70 else "#ffb347" if score >= 40 else "#ff4b4b"
    label = "Strong Match 🟢" if score >= 70 else "Moderate Match 🟡" if score >= 40 else "Weak Match 🔴"

    k1.markdown(
        f"""<div class="score-card">
            <div style="color:#888;font-size:0.8rem;margin-bottom:4px">MATCH SCORE</div>
            <div class="score-number" style="background: linear-gradient(90deg,{color},{color}aa);-webkit-background-clip:text;">{score}%</div>
            <div style="color:{color};font-size:0.85rem;margin-top:4px">{label}</div>
        </div>""",
        unsafe_allow_html=True,
    )
    k2.metric("✅ Skills Matched", f"{result['matched_skills_count']} / {result['total_jd_skills']}")
    k3.metric("🎓 Education Match", result["education_match"])
    k4.metric("💼 Experience Level", result["experience_level"])

    st.markdown("### ")

    # ── Charts Row ─────────────────────────────────────────────────────────────
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<p class="section-header">📈 Section Breakdown</p>', unsafe_allow_html=True)
        fig1 = render_section_scores(result["section_scores"])
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        st.markdown('<p class="section-header">🎯 Skill Coverage</p>', unsafe_allow_html=True)
        fig2 = render_skill_match_chart(result["matched_skills_count"], result["missing_skills_count"])
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ── Skills ─────────────────────────────────────────────────────────────────
    s1, s2 = st.columns(2, gap="large")
    with s1:
        st.markdown('<p class="section-header">✅ Matched Skills</p>', unsafe_allow_html=True)
        if result["matched_skills"]:
            tags = "".join(f'<span class="skill-tag">{s}</span>' for s in result["matched_skills"])
            st.markdown(tags, unsafe_allow_html=True)
        else:
            st.info("No matched skills found.")
    with s2:
        st.markdown('<p class="section-header">❌ Missing Skills</p>', unsafe_allow_html=True)
        if result["missing_skills"]:
            tags = "".join(f'<span class="skill-tag missing-tag">{s}</span>' for s in result["missing_skills"])
            st.markdown(tags, unsafe_allow_html=True)
        else:
            st.success("You have all required skills!")

    st.markdown("---")

    # ── Feedback ───────────────────────────────────────────────────────────────
    st.markdown("### 💡 Actionable Feedback")
    for fb in result["feedback"]:
        ftype = "warning" if "consider" in fb.lower() or "add" in fb.lower() else \
                "error" if "missing" in fb.lower() or "no " in fb.lower() else ""
        st.markdown(f'<div class="feedback-box {ftype}">{fb}</div>', unsafe_allow_html=True)

    # ── Extracted Entities ─────────────────────────────────────────────────────
    with st.expander("🔬 View Extracted Resume Entities (NLP)"):
        e1, e2 = st.columns(2)
        with e1:
            st.markdown("**📌 Named Entities from Resume**")
            for ent_text, ent_label in result.get("entities", []):
                st.markdown(f"`{ent_label}` — {ent_text}")
        with e2:
            st.markdown("**🔑 Top Keywords (TF-IDF)**")
            for kw in result.get("top_keywords", []):
                st.markdown(f"• {kw}")
