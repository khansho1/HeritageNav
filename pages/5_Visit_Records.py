
import streamlit as st
import json

from components import setup_page, page_footer
from database import get_visit_plans


setup_page("Visit Records")

st.title("Saved Visit Records")

plans = get_visit_plans()

if plans:

    display_data = [
        {
            "ID": plan[0],
            "Visitor": plan[1],
            "Destination": plan[2],
            "Date": plan[3],
            "Language": plan[4],
            "Offline Preference": plan[5]
        }
        for plan in plans
    ]

    st.dataframe(
        display_data,
        use_container_width=True
    )

    json_data = json.dumps(
        display_data,
        indent=4,
        ensure_ascii=False
    )

    st.download_button(
        "Download Visit Records",
        data=json_data,
        file_name="visit_records.json",
        mime="application/json"
    )

else:

    st.info("No visit records available.")


page_footer()

