
import streamlit as st

from components import setup_page, page_footer
from database import get_sites


setup_page("Explore Heritage")

st.title("Explore Heritage Sites")

search = st.text_input(
    "Search by monument, city or state"
)

sites = get_sites()

filtered_sites = []

for site in sites:

    searchable_text = (
        site[1] + " " + site[2] + " " + site[3]
    ).lower()

    if search.lower() in searchable_text:
        filtered_sites.append(site)


if filtered_sites:

    for site in filtered_sites:

        with st.expander(
            f"{site[1]} — {site[2]}, {site[3]}"
        ):

            st.write("**Description:**")
            st.write(site[4] or "No description available.")

            st.write(f"**Site ID:** {site[0]}")

else:

    st.warning("No matching heritage sites found.")


page_footer()
