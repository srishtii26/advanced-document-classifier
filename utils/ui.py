
import streamlit as st

def apply_css():

    st.markdown("""
    <style>

    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(
            90deg,
            #00DBDE,
            #FC00FF
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)

