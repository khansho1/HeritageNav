
import streamlit as st
import html

from components import setup_page, page_footer
from database import (
    add_site,
    get_sites,
    update_site,
    delete_site
)


def display_html_table(records):
    """Display a list of dictionaries as a safe HTML table."""

    if not records:
        st.info("No sites available.")
        return

    headers = list(records[0].keys())

    header_html = "".join(
        f"<th>{html.escape(str(header))}</th>"
        for header in headers
    )

    rows_html = ""

    for record in records:
        cells = "".join(
            f"<td>{html.escape(str(record.get(header, '')))}</td>"
            for header in headers
        )

        rows_html += f"<tr>{cells}</tr>"

    table_html = f"""
    <style>
        .heritage-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        .heritage-table th {{
            background-color: #183D2D;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        .heritage-table td {{
            padding: 12px;
            border-bottom: 1px solid #E8E0D0;
            color: #26352D;
        }}
        .heritage-table tr:nth-child(even) {{
            background-color: #F1EEE6;
        }}
    </style>

    <div style="overflow-x:auto;">
        <table class="heritage-table">
            <thead><tr>{header_html}</tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
    """

    st.html(table_html)


# PAGE SETUP
setup_page("Manage Heritage Sites")
st.title("Manage Heritage Sites")


# 1. ADD HERITAGE SITE
st.subheader("1. Add Heritage Site")

with st.form("add_site_form"):

    name = st.text_input("Site Name")
    city = st.text_input("City")
    state = st.text_input("State")
    description = st.text_area("Description")

    submitted = st.form_submit_button("Add Site")

    if submitted:

        if name.strip() and city.strip() and state.strip():

            add_site(name, city, state, description)

            st.success("Site added successfully!")
            st.rerun()

        else:
            st.error("Please fill all required fields.")


st.divider()


# 2. VIEW HERITAGE SITES
st.subheader("2. View Heritage Sites")

sites = get_sites()

if sites:

    display_data = [
        {
            "ID": site[0],
            "Name": site[1],
            "City": site[2],
            "State": site[3],
            "Description": site[4] or ""
        }
        for site in sites
    ]

    display_html_table(display_data)

else:
    st.info("No sites available.")


st.divider()


# 3. UPDATE HERITAGE SITE
st.subheader("3. Update Heritage Site")

if sites:

    site_ids = [site[0] for site in sites]

    selected_id = st.selectbox(
        "Select Site ID",
        site_ids,
        key="update_id"
    )

    selected_site = next(
        site for site in sites if site[0] == selected_id
    )

    with st.form("update_form"):

        new_name = st.text_input(
            "Name",
            value=selected_site[1]
        )

        new_city = st.text_input(
            "City",
            value=selected_site[2]
        )

        new_state = st.text_input(
            "State",
            value=selected_site[3]
        )

        new_description = st.text_area(
            "Description",
            value=selected_site[4] or ""
        )

        update_button = st.form_submit_button("Update Site")

        if update_button:

            if (
                new_name.strip()
                and new_city.strip()
                and new_state.strip()
            ):

                update_site(
                    selected_id,
                    new_name,
                    new_city,
                    new_state,
                    new_description
                )

                st.success("Site updated!")
                st.rerun()

            else:
                st.error("Name, city and state are required.")


st.divider()


# 4. DELETE HERITAGE SITE
st.subheader("4. Delete Heritage Site")

sites = get_sites()

if sites:

    delete_options = {
        f"{site[1]} — {site[2]} (ID: {site[0]})": site[0]
        for site in sites
    }

    selected_delete = st.selectbox(
        "Select Site",
        list(delete_options.keys()),
        key="delete_id"
    )

    confirm = st.checkbox("I confirm deletion.")

    if st.button("Delete Site"):

        if confirm:

            delete_site(delete_options[selected_delete])

            st.success("Site deleted!")
            st.rerun()

        else:
            st.warning("Please confirm before deleting.")


page_footer()
