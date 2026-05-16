
import streamlit as st

from features.chatbot import show_chatbot

from features.analytics_plus import (
    show_advanced_analytics
)

# =========================================
# AI WORKSPACE
# =========================================

def show_ai_workspace():

    st.write("## 🤖 AI Workspace")

    st.info(
        "Unified AI document intelligence workspace"
    )

    # =========================================
    # TABS
    # =========================================

    tab1, tab2, tab3, tab4 = st.tabs([

        "📄 Document",

        "📊 Analytics",

        "🤖 Chatbot",

        "🧠 Insights"
    ])

    # =========================================
    # DOCUMENT TAB
    # =========================================


    with tab1:

        st.write("## 📄 Upload Document")

        uploaded_file = st.file_uploader(
            "Upload TXT or PDF",
            type=["txt", "pdf"]
        )

        if uploaded_file is not None:

            text = ""

            # TXT

            if uploaded_file.type == "text/plain":

                text = uploaded_file.read().decode(
                    "utf-8"
                )

            # PDF

            elif uploaded_file.type == "application/pdf":

                import pdfplumber

                with pdfplumber.open(
                    uploaded_file
                ) as pdf:

                    for page in pdf.pages:

                        extracted = (
                            page.extract_text()
                        )

                        if extracted:

                            text += extracted

            st.session_state.document_text = text

            st.success(
                "✅ Document uploaded successfully"
            )

        if st.session_state.document_text:

            st.text_area(
                "Document Content",
                st.session_state.document_text,
                height=400
            )

        else:

            st.warning(
                "No document uploaded yet."
            )

    # =========================================
    # ANALYTICS TAB
    # =========================================

    with tab2:

        show_advanced_analytics(
            st.session_state.history
        )

    # =========================================
    # CHATBOT TAB
    # =========================================

    with tab3:

        show_chatbot(
            st.session_state.document_text
        )

    # =========================================
    # INSIGHTS TAB
    # =========================================

    with tab4:

        st.write("## 🧠 AI Insights")

        if st.session_state.prediction:

            st.success(
                f"📌 Prediction: "
                f"{st.session_state.prediction}"
            )

            st.info(
                f"🎯 Confidence: "
                f"{st.session_state.confidence:.2f}%"
            )

        else:

            st.warning(
                "No AI analysis available."
            )

        if st.session_state.document_text:

            word_count = len(
                st.session_state.document_text.split()
            )

            st.metric(
                "🧮 Word Count",
                word_count
            )

            st.metric(
                "📄 Characters",
                len(
                    st.session_state.document_text
                )
            )

