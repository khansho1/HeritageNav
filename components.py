
import streamlit as st
from database import init_db


def setup_page(title):

    init_db()

    st.sidebar.title("🏛️ HeritageNav")

    st.sidebar.caption("Explore India's heritage")

    language = st.sidebar.selectbox(
        "Select Language",
        ["English", "Hindi", "Marathi"],
        key="language_selector"
    )

    st.sidebar.caption(f"Language: {language}")
        # Custom website styling
    st.markdown("""
        <style>

        .stButton > button {
            border-radius: 10px;
            font-weight: 600;
            padding: 8px 18px;
        }

        [data-testid="stMetric"] {
            background-color: #F3F4F6;
            padding: 15px;
            border-radius: 12px;
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid #E5E7EB;
        }

        h1, h2, h3 {
            font-weight: 700;
        }

        </style>
    """, unsafe_allow_html=True)

    st.sidebar.divider()

    return language


def page_footer():

    st.divider()
    st.caption("HeritageNav | Student EDI Project")
