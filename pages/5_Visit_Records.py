
import streamlit as st
import json
import html

from components import setup_page, page_footer
from database import get_visit_plans


def display_html_table(records):
    """Display visitor records without using PyArrow."""

    if not records:
        st.info("No visit records available.")
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
        .visit-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        .visit-table th {{
            background-color: #183D2D;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        .visit-table td {{
            padding: 12px;
            border-bottom: 1px solid #E8E0D0;
            color: #26352D;
        }}
        .visit-table tr:nth-child(even) {{
            background-color: #F1EEE6;
        }}
    </style>

    <div style="overflow-x:auto;">
        <table class="visit-table">
            <thead><tr>{header_html}</tr></thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
    """

    st.html(table_html)


# PAGE SETUP
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

    # Display records using HTML
    display_html_table(display_data)

    # Download records as JSON
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
