
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Premium AI Dashboard",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# PREMIUM CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"] {

    font-family: 'Inter', sans-serif;

    background: #0B1120;

    color: white;
}

.main {

    background:
    radial-gradient(
        circle at top left,
        rgba(124,58,237,0.25),
        transparent 35%
    ),

    radial-gradient(
        circle at bottom right,
        rgba(37,99,235,0.25),
        transparent 35%
    ),

    #0B1120;
}

.title {

    text-align: center;

    font-size: 4rem;

    font-weight: 800;

    background: linear-gradient(
        90deg,
        #60A5FA,
        #A78BFA,
        #F472B6
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    margin-bottom: 0.5rem;
}

.subtitle {

    text-align: center;

    color: #CBD5E1;

    font-size: 1.2rem;

    margin-bottom: 2.5rem;
}

.metric-card {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(18px);

    border-radius: 24px;

    padding: 28px;

    transition: 0.3s ease;

    box-shadow:
    0px 8px 30px rgba(0,0,0,0.35);
}

.metric-card:hover {

    transform: translateY(-5px);

    border: 1px solid rgba(255,255,255,0.2);
}

.section-card {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(18px);

    border-radius: 24px;

    padding: 28px;

    margin-bottom: 24px;

    box-shadow:
    0px 8px 30px rgba(0,0,0,0.25);
}

.stButton > button {

    width: 100%;

    border-radius: 16px;

    height: 3.2em;

    border: none;

    font-size: 16px;

    font-weight: 700;

    color: white;

    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );

    transition: 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.02);

    opacity: 0.92;
}

.stTabs [data-baseweb="tab"] {

    background-color: rgba(255,255,255,0.05);

    border-radius: 12px;

    padding: 10px 20px;

    margin-right: 10px;
}

[data-testid="stSidebar"] {

    background: rgba(17,24,39,0.95);

    border-right:
    1px solid rgba(255,255,255,0.08);
}

.stFileUploader {

    background: rgba(255,255,255,0.04);

    padding: 14px;

    border-radius: 18px;

    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("🚀 Premium AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 Analytics",
        "🤖 AI Workspace"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Premium AI-powered analytics interface"
)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<div class="title">'
    '🚀 Premium AI Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Modern SaaS Interface for AI Applications'
    '</div>',
    unsafe_allow_html=True
)

# =========================================
# DASHBOARD
# =========================================

if page == "🏠 Dashboard":

    st.write("## 📈 Overview")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            '''
            <div class="metric-card">
                <h3>📄 Documents</h3>
                <h1>1,284</h1>
                <p>Processed by AI</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '''
            <div class="metric-card">
                <h3>🧠 Accuracy</h3>
                <h1>96.85%</h1>
                <p>Model performance</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            '''
            <div class="metric-card">
                <h3>⚡ AI Engine</h3>
                <h1>BERT + NLP</h1>
                <p>Enterprise-grade</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '''
        <div class="section-card">
            <h2>📄 AI Document Intelligence</h2>

            <p>
            Premium AI-powered document analysis platform
            with OCR, NLP, BERT transformers, analytics,
            reporting and automation.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div class="section-card">
            <h2>✨ Features</h2>

            <ul>
                <li>OCR Image Extraction</li>
                <li>AI Classification</li>
                <li>Interactive Analytics</li>
                <li>PDF Reports</li>
                <li>BERT Insights</li>
                <li>AI Q&A</li>
            </ul>
        </div>
        ''',
        unsafe_allow_html=True
    )

# =========================================
# ANALYTICS
# =========================================

elif page == "📊 Analytics":

    st.write("## 📊 AI Analytics")

    data = pd.DataFrame({

        "Category": [
            "AI",
            "Finance",
            "Healthcare",
            "Cybersecurity",
            "Education"
        ],

        "Confidence": [
            96,
            88,
            82,
            91,
            85
        ]
    })

    fig = px.bar(

        data,

        x="Category",

        y="Confidence",

        text="Confidence",

        title="AI Confidence Scores"
    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        '''
        <div class="section-card">
            <h2>📈 AI Insights</h2>

            <p>
            The AI engine is currently performing
            with exceptionally high confidence levels
            across all categories.
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )

# =========================================
# AI WORKSPACE
# =========================================

elif page == "🤖 AI Workspace":

    st.write("## 🤖 AI Workspace")

    tab1, tab2, tab3 = st.tabs([
        "📂 Upload",
        "📊 Results",
        "🧠 Insights"
    ])

    with tab1:

        st.markdown(
            '''
            <div class="section-card">
                <h3>📂 Upload Documents</h3>

                <p>
                Upload files for premium AI analysis.
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.file_uploader(
            "Upload Files",
            type=["pdf", "txt", "png", "jpg"]
        )

    with tab2:

        st.markdown(
            '''
            <div class="section-card">
                <h2>📊 Analysis Results</h2>

                <h1>AI Document</h1>

                <p>
                Confidence Score: 96.85%
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.progress(96)

        st.toast("✅ Analysis Complete")

    with tab3:

        st.markdown(
            '''
            <div class="section-card">
                <h2>🧠 AI Insights</h2>

                <p>
                This document appears highly technical
                and professionally structured.
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.balloons()

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

