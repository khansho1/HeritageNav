
import streamlit as st
from datetime import date

from components import setup_page, page_footer
from database import get_sites, save_visit_plan


setup_page("Plan Your Visit")

st.title("Plan Your Visit")

sites = get_sites()

if not sites:

    st.warning("Please add heritage sites first.")

else:

    site_names = [site[1] for site in sites]

    with st.form("visit_form"):

        visitor_name = st.text_input("Your Name")

        destination = st.selectbox(
            "Choose Destination",
            site_names
        )

        visit_date = st.date_input(
            "Choose Visit Date",
            min_value=date.today()
        )

        language = st.selectbox(
            "Preferred Language",
            ["English", "Hindi", "Marathi"]
        )

        offline_preference = st.radio(
            "Do you prefer offline information?",
            ["Yes", "No"]
        )

        submitted = st.form_submit_button("Save Visit Plan")

        if submitted:

            if visitor_name.strip():

                save_visit_plan(
                    visitor_name,
                    destination,
                    visit_date,
                    language,
                    offline_preference
                )

                st.success("Your visit plan has been saved!")

            else:

                st.error("Please enter your name.")


page_footer()
