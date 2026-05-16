
import streamlit as st
import pdfplumber
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from sympy import python
from transformers import pipeline
from textblob import TextBlob
from summa.summarizer import summarize
import yake

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from datetime import datetime

from utils.auth import setup_auth
from utils.classifier import classify_document
from utils.pdf_report import generate_pdf
from utils.analytics import show_history
from utils.ocr import extract_text_from_image
from utils.ui import apply_css
from features.premium_ui import apply_premium_ui
from features.resume_matcher import (
    show_resume_matcher
)
from features.chatbot import show_chatbot
from features.analytics_plus import (
    show_advanced_analytics
)
from features.ai_workspace import (
    show_ai_workspace
)

from features.landing_page import (
    show_landing_page
)
from features.voice_ai import (
    show_voice_ai
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Document Intelligence Platform",
    page_icon="📄",
    layout="wide"
)

# =========================================
# APPLY CSS
# =========================================

apply_premium_ui()

# =========================================
# SESSION STATE
# =========================================

if "history" not in st.session_state:
    st.session_state.history = []

if "prediction" not in st.session_state:
    st.session_state.prediction = ""

if "confidence" not in st.session_state:
    st.session_state.confidence = 0

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

# =========================================
# BERT
# =========================================

bert_classifier = pipeline(
    "text-classification"
)

# =========================================
# AUTH
# =========================================

authenticator = setup_auth()

authenticator.login(location="main")

# =========================================
# LOGIN STATUS
# =========================================

if st.session_state.get("authentication_status") == False:

    st.error("❌ Incorrect Username or Password")

elif st.session_state.get("authentication_status") == None:

    st.warning("⚠ Please Login")

elif st.session_state.get("authentication_status"):

    # =========================================
    # HEADER
    # =========================================

    st.markdown(
        '<div class="title">'
        '📄 AI Document Intelligence Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Advanced NLP & Machine Learning Platform'
        '</div>',
        unsafe_allow_html=True
    )

    # =========================================
    # SIDEBAR
    # =========================================

    st.sidebar.title("🚀 Navigation")

    authenticator.logout(location="sidebar")

    page = st.sidebar.radio(
        "Go To",
        [
            "🚀 Landing Page",
            "🏠 Dashboard",
            "📄 AI Classifier",
            "📊 Analytics+",
            "📄 Resume Matcher",
            "🤖 AI Chatbot",
            "🤖 AI Workspace",
            "🎤 Voice AI",
            "ℹ About Project",
        ]
    )

    # =========================================
    # LANDING PAGE
    # =========================================

    if page == "🚀 Landing Page":

        show_landing_page()


    # =========================================
    # DASHBOARD
    # =========================================

    elif page == "🏠 Dashboard":

        st.write("## 🚀 Platform Overview")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.info("📄 Documents Processed")

            st.title(len(st.session_state.history))

        with col2:

            st.success("🧠 AI Accuracy")

            st.title("96.85%")

        with col3:

            st.warning("⚡ AI Model")

            st.title("NLP + BERT")

        st.success("✔ NLP Classification")
        st.success("✔ OCR Image Reading")
        st.success("✔ BERT Transformers")
        st.success("✔ PDF Reports")
        st.success("✔ AI Q&A")

    # =========================================
    # CLASSIFIER
    # =========================================

    elif page == "📄 AI Classifier":

        st.write("## 📄 Upload Document")

        uploaded_file = st.file_uploader(
            "Upload TXT, PDF, or Image",
            type=["txt", "pdf", "png", "jpg", "jpeg"]
        )

        text = st.session_state.document_text

        # TXT

        if uploaded_file is not None:

            if uploaded_file.type == "text/plain":

                text = uploaded_file.read().decode(
                    "utf-8"
                )

            # PDF

            elif uploaded_file.type == "application/pdf":

                text = ""

                with pdfplumber.open(uploaded_file) as pdf:

                    for page_pdf in pdf.pages:

                        extracted = (
                            page_pdf.extract_text()
                        )

                        if extracted:

                            text += extracted

            # IMAGE

            elif uploaded_file.type in [
                "image/png",
                "image/jpeg"
            ]:

                text, image = extract_text_from_image(
                    uploaded_file
                )

                st.image(
                    image,
                    caption="Uploaded Image",
                    use_container_width=True
                )

            st.session_state.document_text = text

        # =========================================
        # TEXT AREA
        # =========================================

        manual_text = st.text_area(
            "📝 Or paste text here",
            value=st.session_state.document_text,
            height=200
        )

        if manual_text:

            text = manual_text

            st.session_state.document_text = text

        # =========================================
        # WORD COUNT
        # =========================================

        if text:

            st.write(
                f"🧮 Word Count: "
                f"{len(text.split())}"
            )

            st.download_button(
                label="⬇ Download Text",
                data=text,
                file_name="document.txt",
                mime="text/plain"
            )

        # =========================================
        # CLASSIFY BUTTON
        # =========================================

        if st.button("🚀 Classify Document"):

            with st.spinner(
                "🧠 AI is analyzing document..."
            ):

                (
                    prediction,
                    probabilities,
                    confidence,
                    categories
                ) = classify_document(text)

                st.session_state.prediction = (
                    prediction
                )

                st.session_state.confidence = (
                    confidence
                )

                st.session_state.history.append({
                    "Category": prediction,
                    "Confidence": round(
                        confidence,
                        2
                    )
                })

                # RESULTS

                st.success(
                    f"📌 Predicted Category: "
                    f"{prediction.upper()}"
                )

                st.info(
                    f"🎯 Confidence: "
                    f"{confidence:.2f}%"
                )

                st.progress(int(confidence))

                # SUMMARY

                st.write("## 🧠 AI Summary")

                try:

                    summary = summarize(
                        text,
                        ratio=0.2
                    )

                    st.write(summary)

                except:

                    st.warning(
                        "Summary generation failed."
                    )

                # KEYWORDS

                st.write("## 🔑 Keywords")

                kw_extractor = (
                    yake.KeywordExtractor(top=10)
                )

                keywords = (
                    kw_extractor.extract_keywords(text)
                )

                st.write(
                    [kw[0] for kw in keywords]
                )

                # SENTIMENT

                st.write("## 😊 Sentiment")

                blob = TextBlob(text)

                sentiment = (
                    blob.sentiment.polarity
                )

                if sentiment > 0:

                    st.success("Positive 😀")

                elif sentiment < 0:

                    st.error("Negative 😔")

                else:

                    st.info("Neutral 😐")

                # BERT

                st.write("## 🧠 BERT Insights")

                try:

                    bert_result = bert_classifier(
                        text[:1000]
                    )

                    st.write(bert_result)

                except:

                    st.warning(
                        "BERT analysis failed."
                    )

                # CHART

                st.write(
                    "## 📊 Interactive Chart"
                )

                plot_df = pd.DataFrame({

                    "Category": categories,

                    "Probability": probabilities
                })

                fig = px.bar(
                    plot_df,
                    x="Category",
                    y="Probability",
                    text="Probability",
                    title="AI Classification Confidence"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                # METADATA

                st.write(
                    "## 🕒 Report Metadata"
                )

                current_time = (
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )

                st.write(
                    f"📅 Generated On: "
                    f"{current_time}"
                )

                st.write(
                    f"🧮 Words: "
                    f"{len(text.split())}"
                )

        # =========================================
        # PDF REPORT
        # =========================================

        if st.session_state.prediction:

            st.write("## 📑 PDF Report")

            if st.button(
                "📄 Generate PDF Report"
            ):

                generate_pdf(
                    st.session_state.prediction,
                    st.session_state.confidence
                )

                with open(
                    "AI_Report.pdf",
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="⬇ Download PDF",
                        data=pdf_file,
                        file_name="AI_Report.pdf",
                        mime="application/pdf"
                    )

            # =========================================
            # Q&A
            # =========================================

            st.write("## 🤖 Ask Questions")

            user_question = st.text_input(
                "Ask about the document"
            )

            if user_question:

                document_text = (
                    st.session_state.document_text
                )

                sentences = (
                    document_text.split('.')
                )

                vectorizer = (
                    TfidfVectorizer()
                )

                vectors = (
                    vectorizer.fit_transform(
                        sentences + [user_question]
                    )
                )

                similarity = (
                    cosine_similarity(
                        vectors[-1],
                        vectors[:-1]
                    )
                )

                index = similarity.argmax()

                answer = sentences[index]

                st.success(answer)

        # =========================================
        # HISTORY
        # =========================================

        st.write("## 🕘 History")

        show_history(
            st.session_state.history
        )

        # =========================================
        # CLEAR HISTORY
        # =========================================

        if st.button("🗑 Clear History"):

            st.session_state.history = []

            st.success("History Cleared!")

    
    
    # =========================================
    # RESUME MATCHER
    # =========================================

    elif page == "📄 Resume Matcher":

        show_resume_matcher()


    # =========================================
    # AI CHATBOT
    # =========================================

    elif page == "🤖 AI Chatbot":

        show_chatbot(
            st.session_state.document_text
        )

    # =========================================
    # ANALYTICS+
    # =========================================

    elif page == "📊 Analytics+":

        show_advanced_analytics(
            st.session_state.history
        )

    # =========================================
    # AI WORKSPACE
    # =========================================

    elif page == "🤖 AI Workspace":

        show_ai_workspace()

    # =========================================
    # VOICE AI
    # =========================================

    elif page == "🎤 Voice AI":

        show_voice_ai()


    # =========================================
    # ABOUT
    # =========================================

    elif page == "ℹ About Project":

        st.write("## ℹ About Project")

        st.markdown("""
        ### 📄 AI Document Intelligence Platform

        Features:
        - NLP Classification
        - OCR Text Extraction
        - BERT Transformers
        - AI Summarization
        - Interactive Charts
        - PDF Reports
        - AI Question Answering
        - CSV Export

        ### 🚀 Developed By
        Srishti S Rao
        """)

    # =========================================
    # FOOTER
    # =========================================

    st.markdown(
        "<hr><center>"
        "Built with ❤️ using AI & NLP"
        "</center>",
        unsafe_allow_html=True
    )

