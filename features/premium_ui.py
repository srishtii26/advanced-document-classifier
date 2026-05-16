
import streamlit as st

def apply_premium_ui():

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

        margin-bottom: 2rem;
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

    .stTextArea textarea {

        border-radius: 18px;

        background: rgba(255,255,255,0.04);

        color: white;
    }

    .stDataFrame {

        border-radius: 18px;
    }

    </style>
    """, unsafe_allow_html=True)

