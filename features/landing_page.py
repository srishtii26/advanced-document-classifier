
import streamlit as st

# =========================================
# LANDING PAGE
# =========================================

def show_landing_page():

    # =========================================
    # HERO SECTION
    # =========================================

    st.markdown(
        '''
        <div style="
            text-align:center;
            padding:60px 20px;
        ">

            <h1 style="
                font-size:4rem;
                font-weight:800;
                background: linear-gradient(
                    90deg,
                    #60A5FA,
                    #A78BFA,
                    #F472B6
                );
                -webkit-background-clip:text;
                -webkit-text-fill-color:transparent;
            ">
                🚀 AI Document Intelligence
            </h1>

            <p style="
                font-size:1.3rem;
                color:#CBD5E1;
                max-width:800px;
                margin:auto;
            ">
                Enterprise AI platform powered by
                OCR, NLP, BERT and intelligent analytics.
            </p>

        </div>
        ''',
        unsafe_allow_html=True
    )

    # =========================================
    # BUTTONS
    # =========================================

    col1, col2, col3 = st.columns([1,1,1])

    with col2:

        st.button("🚀 Launch AI Workspace")

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================
    # STATS
    # =========================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📄 Documents",
            "1,284+"
        )

    with col2:

        st.metric(
            "🧠 Accuracy",
            "96.85%"
        )

    with col3:

        st.metric(
            "⚡ Speed",
            "1.2s"
        )

    with col4:

        st.metric(
            "🤖 AI Models",
            "4"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================
    # FEATURES
    # =========================================

    st.write("## ✨ Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            '''
            <div style="
                background:rgba(255,255,255,0.05);
                padding:24px;
                border-radius:20px;
            ">
                <h2>📄 OCR + NLP</h2>

                <p>
                Extract and analyze
                documents intelligently.
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '''
            <div style="
                background:rgba(255,255,255,0.05);
                padding:24px;
                border-radius:20px;
            ">
                <h2>🤖 AI Chatbot</h2>

                <p>
                Chat with your documents
                using AI assistance.
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            '''
            <div style="
                background:rgba(255,255,255,0.05);
                padding:24px;
                border-radius:20px;
            ">
                <h2>📊 Analytics+</h2>

                <p>
                Enterprise-grade analytics
                and insights dashboard.
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================
    # WHY CHOOSE US
    # =========================================

    st.write("## 🚀 Why Choose This Platform?")

    st.success("✔ AI-Powered Document Analysis")

    st.success("✔ BERT + NLP Intelligence")

    st.success("✔ Interactive AI Workspace")

    st.success("✔ Resume Matcher")

    st.success("✔ Enterprise Analytics")

    st.success("✔ Premium UI/UX")

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================
    # FOOTER
    # =========================================

    st.markdown("---")

    st.markdown(
        "<center>"
        "Built with ❤️ using AI & Streamlit"
        "</center>",
        unsafe_allow_html=True
    )

