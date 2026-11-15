
import streamlit as st
from datetime import date

from components import setup_page, page_footer
from database import get_sites, save_visit_plan
from pathlib import Path

# =====================================
# PAGE SETUP
# =====================================

setup_page("Plan Your Visit")
IMAGE_DIR = Path(__file__).resolve().parent.parent / "images"

image_files = {
    "taj mahal": "taj_mahal.jpg",
    "red fort": "red_fort.jpg",
    "gateway of india": "gateway_of_india.jpg"
}
st.title("Plan Your Visit")

st.write(
    "Choose your destination and prepare for your heritage journey."
)

sites = get_sites()


# =====================================
# CHECK DESTINATIONS
# =====================================

if not sites:

    st.warning("Please add heritage sites first.")

else:

    site_names = [site[1] for site in sites]

    # Receive destination from Explore Heritage
    selected_destination = st.session_state.pop(
        "selected_destination",
        None
    )

    if selected_destination:

        selected_name = selected_destination["name"]

        if selected_name in site_names:
            st.session_state["plan_destination"] = selected_name

    # =================================
    # DESTINATION SELECTION
    # =================================

    st.subheader("1. Choose Your Destination")

    destination = st.selectbox(
        "Select a heritage site",
        site_names,
        key="plan_destination"
    )

    # Find selected destination record
    selected_site = next(
        (site for site in sites if site[1] == destination),
        None
    )

    # =================================
    # DESTINATION PREVIEW
    # =================================

    if selected_site:

        city = selected_site[2]
        state = selected_site[3]
        description = selected_site[4]

        with st.container(border=True):
            st.caption("YOUR SELECTED DESTINATION")
            st.subheader(f"🏛️ {destination}")

            # Find and display the destination image
            image_name = image_files.get(destination.lower().strip())

            if image_name:
                image_path = IMAGE_DIR / image_name

                if image_path.exists():
                    st.image(str(image_path), width="stretch")

            st.write(f"📍 **Location:** {city}, {state}")
            st.write(description or "No description available.")

    st.write("")

    # =================================
    # VISIT PLANNING FORM
    # =================================

    st.subheader("2. Your Travel Details")

    with st.form("visit_form"):

        visitor_name = st.text_input(
            "Your Name",
            placeholder="Enter your name"
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

        st.divider()

        submitted = st.form_submit_button(
            "📅 Save Visit Plan",
            width="stretch"
        )

        # =================================
        # SAVE VISIT PLAN
        # =================================

        if submitted:

            if visitor_name.strip():

                save_visit_plan(
                    visitor_name,
                    destination,
                    visit_date,
                    language,
                    offline_preference
                )

                st.success(
                    f"Your visit plan for {destination} has been saved!"
                )

                st.balloons()

            else:

                st.error("Please enter your name.")


# =====================================
# VISITOR TRAVEL CHECKLIST
# =====================================

st.divider()

st.subheader("3. Travel Preparation Checklist")

st.write(
    "Prepare these essentials before starting your journey."
)

checklist_items = [
    "Carry a water bottle",
    "Wear comfortable walking shoes",
    "Carry a valid ID card",
    "Charge your mobile phone",
    "Carry a power bank",
    "Check monument opening timings",
    "Keep your tickets or booking details ready",
    "Carry a camera if needed"
]

completed_tasks = 0

col1, col2 = st.columns(2)

for index, item in enumerate(checklist_items):

    with (col1 if index % 2 == 0 else col2):

        checked = st.checkbox(
            item,
            key=f"travel_check_{index}"
        )

        if checked:
            completed_tasks += 1


# Progress calculation
total_tasks = len(checklist_items)

progress = completed_tasks / total_tasks

st.write("")

st.progress(progress)

st.caption(
    f"{completed_tasks} out of {total_tasks} tasks completed"
)

if completed_tasks == total_tasks:

    st.success(
        "🎉 You're ready for your heritage journey!"
    )

elif completed_tasks > 0:

    st.info(
        "Good progress! Complete the remaining tasks."
    )

else:

    st.caption(
        "Start checking items as you prepare for your visit."
    )

# =====================================
# FOOTER
# =====================================

page_footer()
