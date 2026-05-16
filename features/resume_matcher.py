
import streamlit as st

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

# =========================================
# RESUME MATCHER
# =========================================

def show_resume_matcher():

    st.write("## 📄 AI Resume Matcher")

    st.info(
        "Compare Resume with Job Description"
    )

    resume = st.text_area(
        "📄 Paste Resume",
        height=250
    )

    job_description = st.text_area(
        "💼 Paste Job Description",
        height=250
    )

    if st.button("🚀 Analyze Resume"):

        if resume and job_description:

            documents = [
                resume,
                job_description
            ]

            tfidf = TfidfVectorizer()

            tfidf_matrix = tfidf.fit_transform(
                documents
            )

            similarity = cosine_similarity(
                tfidf_matrix[0:1],
                tfidf_matrix[1:2]
            )

            score = round(
                similarity[0][0] * 100,
                2
            )

            st.success(
                f"🎯 ATS Match Score: {score}%"
            )

            st.progress(int(score))

            # =========================================
            # SKILL ANALYSIS
            # =========================================

            skills = [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "AI",
                "SQL",
                "Communication",
                "Leadership",
                "Data Analysis",
                "Cybersecurity",
                "Cloud"
            ]

            matched_skills = []

            missing_skills = []

            for skill in skills:

                if (
                    skill.lower()
                    in resume.lower()
                ):

                    matched_skills.append(skill)

                elif (
                    skill.lower()
                    in job_description.lower()
                ):

                    missing_skills.append(skill)

            st.write(
                "## ✅ Skills Found"
            )

            st.write(matched_skills)

            st.write(
                "## ❌ Missing Skills"
            )

            st.write(missing_skills)

            # =========================================
            # AI RECOMMENDATION
            # =========================================

            st.write(
                "## 🧠 AI Recommendation"
            )

            if score >= 80:

                st.success(
                    "Excellent match for this role 🚀"
                )

            elif score >= 60:

                st.warning(
                    "Good match but can improve."
                )

            else:

                st.error(
                    "Resume needs optimization."
                )

        else:

            st.warning(
                "Please paste both fields."
            )

