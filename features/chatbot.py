
import streamlit as st
import time

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

# =========================================
# PREMIUM AI CHATBOT
# =========================================

def show_chatbot(document_text):

    st.write("## 🤖 AI Chat Assistant")

    st.info(
        "Ask questions about your uploaded document"
    )

    # =========================================
    # SUGGESTED QUESTIONS
    # =========================================

    st.write("### 💡 Suggested Questions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.button(
            "📄 Summarize Document"
        )

    with col2:

        st.button(
            "🧠 Key Insights"
        )

    with col3:

        st.button(
            "⚡ Technologies Used"
        )

    # =========================================
    # CHAT HISTORY
    # =========================================

    if "messages" not in st.session_state:

        st.session_state.messages = []

    # =========================================
    # DISPLAY CHAT
    # =========================================

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    # =========================================
    # USER INPUT
    # =========================================

    prompt = st.chat_input(
        "Ask something about the document..."
    )

    if prompt:

        # USER MESSAGE

        st.session_state.messages.append({

            "role": "user",

            "content": prompt
        })

        with st.chat_message("user"):

            st.markdown(prompt)

        # =========================================
        # AI RESPONSE
        # =========================================

        with st.chat_message("assistant"):

            with st.spinner(
                "AI is thinking..."
            ):

                time.sleep(1)

                if document_text:

                    sentences = (
                        document_text.split('.')
                    )

                    vectorizer = (
                        TfidfVectorizer()
                    )

                    vectors = (
                        vectorizer.fit_transform(
                            sentences + [prompt]
                        )
                    )

                    similarity = (
                        cosine_similarity(
                            vectors[-1],
                            vectors[:-1]
                        )
                    )

                    index = (
                        similarity.argmax()
                    )

                    answer = (
                        sentences[index]
                    )

                else:

                    answer = (
                        "Please upload a document first."
                    )

                st.markdown(answer)

        # SAVE RESPONSE

        st.session_state.messages.append({

            "role": "assistant",

            "content": answer
        })

    # =========================================
    # CLEAR CHAT
    # =========================================

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

