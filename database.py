import streamlit as st
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "heritagenav.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visit_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visitor_name TEXT NOT NULL,
            destination TEXT NOT NULL,
            visit_date TEXT,
            language TEXT,
            offline_preference TEXT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM sites")
    count = cursor.fetchone()[0]

    if count == 0:

        sample_sites = [
            (
                "Taj Mahal",
                "Agra",
                "Uttar Pradesh",
                "A famous white marble monument built by Shah Jahan."
            ),
            (
                "Red Fort",
                "Delhi",
                "Delhi",
                "A historic Mughal fort in Old Delhi."
            ),
            (
                "Gateway of India",
                "Mumbai",
                "Maharashtra",
                "A famous monument overlooking the Arabian Sea."
            )
        ]

        cursor.executemany("""
            INSERT INTO sites (name, city, state, description)
            VALUES (?, ?, ?, ?)
        """, sample_sites)

    conn.commit()
    conn.close()


def add_site(name, city, state, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sites (name, city, state, description)
        VALUES (?, ?, ?, ?)
    """, (name, city, state, description))

    conn.commit()
    st.cache_data.clear()
    conn.close()

@st.cache_data(ttl=60)

def get_sites():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sites ORDER BY id")

    records = cursor.fetchall()
    conn.close()

    return records


def update_site(site_id, name, city, state, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE sites
        SET name = ?, city = ?, state = ?, description = ?
        WHERE id = ?
    """, (name, city, state, description, site_id))

    conn.commit()
    st.cache_data.clear()
    conn.close()


def delete_site(site_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sites WHERE id = ?",
        (site_id,)
    )

    conn.commit()
    st.cache_data.clear()
    conn.close()


def save_visit_plan(visitor, destination, visit_date,
                    language, offline_preference):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO visit_plans
        (visitor_name, destination, visit_date, language,
         offline_preference)
        VALUES (?, ?, ?, ?, ?)
    """, (
        visitor,
        destination,
        str(visit_date),
        language,
        offline_preference
    ))

    conn.commit()
    st.cache_data.clear()
    conn.close()

@st.cache_data(ttl=60)
def get_visit_plans():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM visit_plans
        ORDER BY id DESC
    """)

    records = cursor.fetchall()
    conn.close()

    return records
