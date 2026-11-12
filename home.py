
import streamlit as st
from pathlib import Path

from components import setup_page, page_footer
from database import get_sites


setup_page("Home")

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


st.title("🏛️ HeritageNav")

st.caption(
    "Discover India's heritage. Explore history. Plan your journey."
)

st.markdown("""
Welcome to **HeritageNav**, your digital companion for exploring
India's historical places and cultural heritage.
""")

st.divider()

col1, col2 = st.columns([2, 1])

with col1:

    st.subheader("History is waiting to be explored")

    st.write("""
    Discover historical monuments, learn their stories,
    explore destinations and plan your next visit.

    HeritageNav aims to make heritage information accessible
    and easy to explore.
    """)

    st.info(
        "Choose a page from the sidebar to get started."
    )

with col2:

    image_path = IMAGE_DIR / "taj_mahal.jpg"

    if image_path.exists():
        st.image(image_path, use_container_width=True)
    else:
        st.info("Add taj_mahal.jpg to the images folder.")

st.divider()

st.subheader("HeritageNav Overview")

sites = get_sites()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Heritage Sites", len(sites))

with col2:
    st.metric("Languages", 3)

with col3:
    st.metric("Project", "EDI")

st.divider()

st.subheader("Featured Destinations")

col1, col2 = st.columns(2)

with col1:

    image_path = IMAGE_DIR / "red_fort.jpg"

    if image_path.exists():
        st.image(image_path, use_container_width=True)

    st.write("**Red Fort — Delhi**")
    st.write("Explore the history of the Mughal era.")

with col2:

    image_path = IMAGE_DIR / "gateway_of_india.jpg"

    if image_path.exists():
        st.image(image_path, use_container_width=True)

    st.write("**Gateway of India — Mumbai**")
    st.write("Discover one of Mumbai's famous landmarks.")

page_footer()
