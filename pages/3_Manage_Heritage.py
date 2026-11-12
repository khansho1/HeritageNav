
import streamlit as st

from components import setup_page, page_footer

from database import (
    add_site,
    get_sites,
    update_site,
    delete_site
)


setup_page("Manage Heritage Sites")

st.title("Manage Heritage Sites")


# CREATE

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


# READ

st.subheader("2. View Heritage Sites")

sites = get_sites()

if sites:

    display_data = [
        {
            "ID": site[0],
            "Name": site[1],
            "City": site[2],
            "State": site[3],
            "Description": site[4]
        }
        for site in sites
    ]

    st.dataframe(
        display_data,
        use_container_width=True
    )

else:

    st.info("No sites available.")


st.divider()


# UPDATE

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


# DELETE

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
