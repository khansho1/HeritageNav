
import streamlit as st
from pathlib import Path

from components import setup_page, page_footer, render_html
from database import get_sites


# =====================================
# PAGE SETUP
# =====================================

setup_page("Home")

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

# Load heritage sites from database
sites = get_sites()


# =====================================
# HERO SECTION
# =====================================

render_html("""
    <div style="padding: 12px 0 20px 0;">

        <div style="
            color: #A87932;
            font-size: 12px;
            font-weight: bold;
            letter-spacing: 3px;
            margin-bottom: 12px;
        ">
            DISCOVER INDIA'S CULTURAL TREASURES
        </div>

        <div style="
            font-family: Georgia, serif;
            font-size: clamp(38px, 5vw, 62px);
            line-height: 1.12;
            font-weight: bold;
            color: #183D2D;
        ">
            Every monument<br>
            has a story to tell.
        </div>

        <div style="
            color: #68776B;
            font-size: 17px;
            margin-top: 18px;
            max-width: 650px;
            line-height: 1.7;
        ">
            Discover India's remarkable heritage, explore historic
            destinations and plan meaningful journeys through time.
        </div>

    </div>
""")


# =====================================
# HERO IMAGE
# =====================================

taj_image = IMAGE_DIR / "taj_mahal.jpg"

if taj_image.exists():
    st.image(
        str(taj_image),
        use_container_width=True
    )
else:
    st.warning(
        "Taj Mahal image not found. "
        "Please add taj_mahal.jpg to the images folder."
    )


# =====================================
# EXPLORE BUTTON
# =====================================

st.write("")

button_col, empty_col = st.columns([1, 4])

with button_col:

    if st.button(
        "Explore Heritage →",
        use_container_width=True
    ):
        st.switch_page("pages/1_Explore_Heritage.py")


st.write("")
st.divider()


# =====================================
# OVERVIEW SECTION
# =====================================

render_html("""
    <div style="margin-bottom: 20px;">

        <div style="
            color: #A87932;
            font-size: 11px;
            font-weight: bold;
            letter-spacing: 2px;
        ">
            YOUR HERITAGE COMPANION
        </div>

        <div style="
            font-family: Georgia, serif;
            font-size: 30px;
            color: #183D2D;
            font-weight: bold;
        ">
            Explore. Learn. Experience.
        </div>

    </div>
""")


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🏛️ Heritage Sites",
        len(sites)
    )

with col2:
    st.metric(
        "🌐 Languages",
        "3"
    )

with col3:
    st.metric(
        "🧭 Project",
        "HeritageNav"
    )


st.write("")
st.divider()


# =====================================
# FEATURED DESTINATIONS
# =====================================

render_html("""
    <div style="margin-bottom: 22px;">

        <div style="
            color: #A87932;
            font-size: 11px;
            font-weight: bold;
            letter-spacing: 2px;
        ">
            PLACES WORTH DISCOVERING
        </div>

        <div style="
            font-family: Georgia, serif;
            font-size: 30px;
            color: #183D2D;
            font-weight: bold;
        ">
            Featured destinations
        </div>

        <div style="color: #68776B;">
            A glimpse into India's incredible past.
        </div>

    </div>
""")


col1, col2 = st.columns(2, gap="large")


# Red Fort card
with col1:

    with st.container(border=True):

        red_fort_image = IMAGE_DIR / "red_fort.jpg"

        if red_fort_image.exists():
            st.image(
                str(red_fort_image),
                use_container_width=True
            )
        else:
            st.info("Add red_fort.jpg to the images folder.")

        st.markdown("### Red Fort")

        st.caption("📍 Delhi · Mughal heritage")

        st.write(
            "Explore the magnificent fort that reflects "
            "the grandeur of the Mughal era."
        )


# Gateway of India card
with col2:

    with st.container(border=True):

        gateway_image = IMAGE_DIR / "gateway_of_india.jpg"

        if gateway_image.exists():
            st.image(
                str(gateway_image),
                use_container_width=True
            )
        else:
            st.info(
                "Add gateway_of_india.jpg to the images folder."
            )

        st.markdown("### Gateway of India")

        st.caption("📍 Mumbai · Colonial heritage")

        st.write(
            "Discover one of Mumbai's most iconic "
            "landmarks overlooking the Arabian Sea."
        )


st.write("")
st.divider()


# =====================================
# WHY HERITAGENAV?
# =====================================

render_html("""
    <div style="
        font-family: Georgia, serif;
        font-size: 28px;
        font-weight: bold;
        color: #183D2D;
        margin-bottom: 18px;
    ">
        More than just a travel guide.
    </div>
""")


col1, col2, col3 = st.columns(3, gap="large")


with col1:
    st.markdown("### 🌍 Explore")

    st.write(
        "Discover historic places and learn about "
        "their cultural significance."
    )


with col2:
    st.markdown("### 🗓️ Plan")

    st.write(
        "Organise your visits and keep track "
        "of your travel plans."
    )


with col3:
    st.markdown("### 🧭 Navigate")

    st.write(
        "Explore location details and experiment "
        "with distance and direction calculations."
    )


# =====================================
# FOOTER
# =====================================

page_footer()
