import streamlit as st

st.set_page_config(page_title="AI Career Recommender")

st.title("🚀 AI Career Path Recommender")

skills_input = st.text_input("Enter your skills (comma separated)")

if st.button("Find Career"):
    skills = skills_input.lower()

    st.subheader("🎯 Recommended Careers")

    if "python" in skills and "machine learning" in skills:
        st.success("AI/ML Engineer")
        st.write("💰 Salary: 6–15 LPA")
        st.write("🛠 Skills to learn: Deep Learning, NLP, Projects")
        st.write("📚 Roadmap:")
        st.write("1. Python strong karo")
        st.write("2. ML algorithms")
        st.write("3. Deep learning")
        st.write("4. Projects + Kaggle")

    if "python" in skills and "data" in skills:
        st.success("Data Scientist")
        st.write("💰 Salary: 5–12 LPA")
        st.write("🛠 Skills: Pandas, ML, Visualization")
        st.write("📚 Roadmap:")
        st.write("1. Pandas & Numpy")
        st.write("2. ML models")
        st.write("3. EDA projects")

    if "html" in skills or "css" in skills:
        st.success("Frontend Developer")
        st.write("💰 Salary: 4–10 LPA")
        st.write("🛠 Skills: React, JS")
        st.write("📚 Roadmap:")
        st.write("1. HTML CSS JS")
        st.write("2. React")
        st.write("3. Projects")

    if skills == "":
        st.warning("Enter skills first")