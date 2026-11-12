
import streamlit as st
import sqlite3

from components import setup_page, page_footer

from database import get_sites, get_connection

from utils import (
    sites_to_csv,
    sites_to_json,
    read_csv_file,
    read_json_file
)


setup_page("Data Import and Export")

st.title("Data Import and Export")

sites = get_sites()


# CSV EXPORT

st.subheader("1. Download CSV")

csv_data = sites_to_csv(sites)

st.download_button(
    "Download CSV",
    data=csv_data,
    file_name="heritage_sites.csv",
    mime="text/csv"
)


# JSON EXPORT

st.divider()

st.subheader("2. Download JSON")

json_data = sites_to_json(sites)

st.download_button(
    "Download JSON",
    data=json_data,
    file_name="heritage_sites.json",
    mime="application/json"
)


# CSV IMPORT

st.divider()

st.subheader("3. Import CSV")

csv_file = st.file_uploader(
    "Upload CSV",
    type=["csv"],
    key="csv_upload"
)

if csv_file is not None:

    try:

        rows = read_csv_file(csv_file)

        st.dataframe(rows)

        if st.button("Save CSV Records"):

            conn = get_connection()
            cursor = conn.cursor()

            count = 0

            for row in rows:

                name = row.get("name", "").strip()
                city = row.get("city", "").strip()
                state = row.get("state", "").strip()
                description = row.get("description", "")

                if name and city and state:

                    cursor.execute("""
                        INSERT INTO sites
                        (name, city, state, description)
                        VALUES (?, ?, ?, ?)
                    """, (name, city, state, description))

                    count += 1

            conn.commit()
            conn.close()

            st.success(f"{count} records imported.")

            st.rerun()

    except Exception as error:

        st.error(str(error))


# JSON IMPORT

st.divider()

st.subheader("4. Import JSON")

json_file = st.file_uploader(
    "Upload JSON",
    type=["json"],
    key="json_upload"
)

if json_file is not None:

    try:

        rows = read_json_file(json_file)

        st.json(rows)

        if st.button("Save JSON Records"):

            conn = get_connection()
            cursor = conn.cursor()

            count = 0

            for row in rows:

                if not isinstance(row, dict):
                    continue

                name = str(row.get("name", "")).strip()
                city = str(row.get("city", "")).strip()
                state = str(row.get("state", "")).strip()
                description = str(row.get("description", ""))

                if name and city and state:

                    cursor.execute("""
                        INSERT INTO sites
                        (name, city, state, description)
                        VALUES (?, ?, ?, ?)
                    """, (name, city, state, description))

                    count += 1

            conn.commit()
            conn.close()

            st.success(f"{count} records imported.")

            st.rerun()

    except Exception as error:

        st.error(str(error))


page_footer()
