
import streamlit as st
import textwrap
from database import init_db


def render_html(content):
    """Render HTML directly without Markdown formatting."""
    st.html(textwrap.dedent(content))

def setup_page(title):

    # Initialize database
    init_db()

    # Browser tab title and page settings are handled by app.py.
    # Global website CSS
    render_html("""
        <style>
        .stApp {
            background-color: #FAF8F3;
            color: #26352D;
        }

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3 {
            color: #183D2D !important;
            font-family: Georgia, serif;
            font-weight: 700;
        }

        h1 {
            letter-spacing: -1px;
        }

        p {
            color: #38483E;
        }

        [data-testid="stSidebar"] {
            background-color: #183D2D;
            border-right: 1px solid #D6C7A1;
        }

        [data-testid="stSidebar"] * {
            color: #F8F5EA;
        }

        [data-testid="stSidebar"] hr {
            border-color: #526B59;
        }

        .stButton > button {
            background-color: #B58A45;
            color: white !important;
            border: none;
            border-radius: 9px;
            padding: 0.65rem 1.2rem;
            font-weight: 600;
            transition: 0.2s ease;
        }

        .stButton > button:hover {
            background-color: #967039;
            color: white !important;
            border: none;
            transform: translateY(-2px);
        }

        [data-testid="stMetric"] {
            background-color: #FFFFFF;
            border: 1px solid #E8E0D0;
            border-radius: 14px;
            padding: 18px;
            box-shadow: 0 3px 12px rgba(30, 50, 35, 0.04);
        }

        [data-testid="stMetricLabel"] {
            color: #68776B !important;
        }

        [data-testid="stMetricValue"] {
            color: #183D2D !important;
        }

        [data-testid="stImage"] img {
            border-radius: 12px;
        }

        [data-testid="stDataFrame"] {
            border: 1px solid #E8E0D0;
            border-radius: 10px;
        }

        a {
            color: #A87932 !important;
        }

        hr {
            border-color: #E7DFD0;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
        </style>
    """)

    # Sidebar branding
    render_html("""
        <div style="padding: 12px 0 5px 0;">
            <div style="font-size: 30px;">🏛️</div>

            <div style="
                font-family: Georgia, serif;
                font-size: 25px;
                font-weight: bold;
                color: #F3D69A;
            ">
                HeritageNav
            </div>

            <div style="
                font-size: 11px;
                color: #D6DCCF;
                letter-spacing: 1px;
            ">
                EXPLORE • DISCOVER • PRESERVE
            </div>
        </div>
    """)

    st.sidebar.divider()

    language = st.sidebar.selectbox(
        "🌐 Select Language",
        ["English", "Hindi", "Marathi"],
        key="language_selector"
    )

    st.sidebar.caption(f"Current language: {language}")

    st.sidebar.divider()

    return language


def page_footer():

    st.divider()

    render_html("""
        <div style="
            text-align: center;
            color: #788276;
            font-size: 13px;
            padding: 12px;
        ">
            🏛️ HeritageNav · Discover India's Living History

            <br>

            <span style="font-size: 11px;">
                A student EDI project
            </span>
        </div>
    """)
