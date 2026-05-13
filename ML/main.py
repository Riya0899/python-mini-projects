import streamlit as st
import pdfplumber
from google import genai
from google.genai import types
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client(api_key="AIzaSyCnB_tPFMUp2QdTgxQmREnrcc5iVoorv-Y")

def get_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=[text],
        config=types.EmbedContentConfig(
            task_type="SEMANTIC_SIMILARITY"
        )
    )
    return result.embeddings[0].values


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def classify_resume(resume_text):
    resume_embedding = get_embedding(resume_text)
    similarities = cosine_similarity(
        [resume_embedding],
        role_vectors
    )[0]
    best_index = similarities.argmax()
    return role_names[best_index], similarities


roles = {
    "Software Engineer": "coding programming java python data structures",
    "Data Scientist": "machine learning statistics pandas numpy data analysis",
    "Machine Learning Engineer": "deep learning tensorflow pytorch mlops ai",
    "Frontend Developer": "html css javascript react ui ux"
}

role_names = list(roles.keys())
role_texts = list(roles.values())

role_embeddings = client.models.embed_content(
    model="gemini-embedding-001",
    contents=role_texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

role_vectors = [e.values for e in role_embeddings.embeddings]

def extract_skills(text):
    skills_db = ["python", "java", "tensorflow", "pytorch", "react", "sql", "ml", "ai"]
    found = []
    text = text.lower()
    for skill in skills_db:
        if skill in text:
            found.append(skill)
    return found


st.set_page_config(layout="centered", page_title="Resume Sorter")

st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}
.result-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 10px;
    margin-top: 15px;
}
.tag {
    display: inline-block;
    background-color: #2d3748;
    padding: 6px 12px;
    border-radius: 8px;
    margin: 5px;
    font-size: 12px;
}
.stButton>button {
    background-color: #3b82f6;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("## 📄 Resume Sorter")
st.caption("Upload a resume PDF to classify it into a tech role.")
st.markdown('<div class="card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
st.markdown('</div>', unsafe_allow_html=True)


if uploaded_file:
    st.success(f"✅ File received: {uploaded_file.name}")
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Classify Resume"):
        role, scores = classify_resume(resume_text)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Result")
        st.markdown(f"""
        <div class="result-box">
            <h4 style="color:#9ca3af;">PREDICTED ROLE</h4>
            <h2>{role}</h2>
        </div>
        """, unsafe_allow_html=True)

        
        skills = extract_skills(resume_text)
        st.write("### Skills detected")
        skills_html = "".join([f'<span class="tag">{skill}</span>' for skill in skills])
        st.markdown(skills_html, unsafe_allow_html=True)

