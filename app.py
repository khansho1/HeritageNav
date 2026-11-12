
import streamlit as st

# Website configuration
st.set_page_config(
    page_title="HeritageNav",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define all website pages
pages = [
    st.Page(
        "home.py",
        title="Home",
        icon="🏠",
        default=True
    ),

    st.Page(
        "pages/1_Explore_Heritage.py",
        title="Explore Heritage",
        icon="🗺️"
    ),

    st.Page(
        "pages/2_Plan_Your_Visit.py",
        title="Plan Your Visit",
        icon="📅"
    ),

    st.Page(
        "pages/3_Manage_Heritage.py",
        title="Manage Heritage",
        icon="⚙️"
    ),

    st.Page(
        "pages/4_Data_Import_Export.py",
        title="Data Import / Export",
        icon="📂"
    ),

    st.Page(
        "pages/5_Visit_Records.py",
        title="Visit Records",
        icon="📋"
    ),

    st.Page(
        "pages/6_About.py",
        title="About",
        icon="ℹ️"
    ),
        st.Page(
        "pages/7_Route_Navigation.py",
        title="Route Navigation",
        icon="🧭"
    )
]

# Create sidebar navigation
navigation = st.navigation(
    pages,
    position="sidebar"
)

# Run selected page
navigation.run()
