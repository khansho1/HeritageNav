
import streamlit as st

from components import setup_page, page_footer


setup_page("About HeritageNav")

st.title("About HeritageNav")

st.write("""
HeritageNav is a student EDI project designed to make
exploring India's historical places and cultural heritage easier.
""")

st.subheader("Our Goals")

st.write("""
- Provide heritage-site information.
- Support multilingual content.
- Help users plan visits.
- Develop an offline information system.
- Explore future hardware-based navigation.
""")

st.subheader("Technologies Used")

st.write("""
- Python
- Streamlit
- SQLite
- JSON
- CSV
""")

st.info("""
This is a learning prototype. It does not yet provide live GPS,
automatic translation, Bluetooth hardware connectivity,
turn-by-turn navigation or downloaded offline map tiles.
""")

page_footer()
