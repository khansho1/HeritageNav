
import streamlit as st
from pathlib import Path

from components import setup_page, page_footer, render_html
from database import get_sites


# =====================================
# PAGE SETUP
# =====================================

setup_page("Explore Heritage")

IMAGE_DIR = Path(__file__).resolve().parent.parent / "images"

sites = get_sites()


# =====================================
# PAGE HEADING
# =====================================

render_html("""
    <div style="padding: 10px 0 22px 0;">
        <div style="
            color: #A87932;
            font-size: 12px;
            font-weight: bold;
            letter-spacing: 3px;
            margin-bottom: 12px;
        ">
            INDIA'S CULTURAL COLLECTION
        </div>

        <div style="
            font-family: Georgia, serif;
            font-size: clamp(34px, 4vw, 48px);
            font-weight: bold;
            color: #183D2D;
            line-height: 1.2;
        ">
            Explore Heritage
        </div>

        <div style="
            color: #68776B;
            font-size: 16px;
            line-height: 1.7;
            max-width: 700px;
            margin-top: 12px;
        ">
            From magnificent forts to timeless monuments,
            discover the places that tell India's story.
        </div>
    </div>
""")


# =====================================
# SEARCH AND FILTER
# =====================================

st.subheader("Find your destination")

col1, col2 = st.columns([2, 1])

with col1:
    search = st.text_input(
        "Search heritage sites",
        placeholder="Try Taj Mahal, Delhi, Maharashtra...",
        key="heritage_search"
    )

with col2:
    available_states = sorted({
        str(site[3]).strip()
        for site in sites
        if len(site) > 3 and site[3]
    })

    state_options = ["All States"] + available_states

    selected_state = st.selectbox(
        "Filter by state",
        state_options,
        key="heritage_state_filter"
    )


# =====================================
# FILTER RECORDS
# =====================================

filtered_sites = []

for site in sites:
    site_id = site[0]
    name = str(site[1] or "")
    city = str(site[2] or "")
    state = str(site[3] or "")
    description = str(site[4] or "")

    searchable_text = (
        name + " " + city + " " + state + " " + description
    ).lower()

    matches_search = search.strip().lower() in searchable_text

    matches_state = (
        selected_state == "All States"
        or state == selected_state
    )

    if matches_search and matches_state:
        filtered_sites.append(site)


filtered_sites.sort(
    key=lambda site: str(site[1] or "").lower()
)


# =====================================
# RESULTS SUMMARY
# =====================================

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.metric("Heritage Sites Found", len(filtered_sites))

with col2:
    st.metric("States Available", len(available_states))

st.divider()


# =====================================
# DESTINATION CARDS
# =====================================

render_html("""
    <div style="margin-bottom: 20px;">
        <div style="
            color: #A87932;
            font-size: 11px;
            font-weight: bold;
            letter-spacing: 2px;
        ">
            DISCOVER SOMETHING HISTORIC
        </div>

        <div style="
            font-family: Georgia, serif;
            font-size: 28px;
            font-weight: bold;
            color: #183D2D;
        ">
            Your destinations
        </div>
    </div>
""")


if filtered_sites:

    image_files = {
        "taj mahal": "taj_mahal.jpg",
        "red fort": "red_fort.jpg",
        "gateway of india": "gateway_of_india.jpg"
    }
    destination_info = {
    "taj mahal": {
        "history": "Built by Mughal emperor Shah Jahan in memory of his wife Mumtaz Mahal. It is one of the finest examples of Mughal architecture.",
        "highlights": [
            "White marble architecture",
            "Beautiful gardens and reflecting pool",
            "Intricate marble inlay work"
        ],
        "tips": [
            "Visit early in the morning for a peaceful experience.",
            "Wear comfortable walking shoes.",
            "Check current visiting rules and ticket details before travelling."
        ]
    },

    "red fort": {
        "history": "Commissioned by Mughal emperor Shah Jahan and completed in 1648. It served as the main residence of Mughal emperors for generations.",
        "highlights": [
            "Lahori Gate",
            "Diwan-i-Aam and Diwan-i-Khas",
            "Mughal gardens and architecture"
        ],
        "tips": [
            "Allow enough time to explore the complex.",
            "Carry water and wear comfortable shoes.",
            "Check current entry timings before visiting."
        ]
    },

    "gateway of india": {
        "history": "Built in Mumbai to commemorate the 1911 visit of King George V and Queen Mary. The monument was completed in 1924.",
        "highlights": [
            "Indo-Saracenic architectural style",
            "Views of the Arabian Sea",
            "Historic waterfront location"
        ],
        "tips": [
            "Enjoy the waterfront views.",
            "Avoid peak crowds if you prefer a quieter visit.",
            "Check local conditions before planning your visit."
        ]
    }
}

    for index in range(0, len(filtered_sites), 2):

        card_columns = st.columns(2, gap="small")

        for column_index, column in enumerate(card_columns):

            site_index = index + column_index

            if site_index >= len(filtered_sites):
                continue

            site = filtered_sites[site_index]

            site_id = site[0]
            name = str(site[1] or "Unnamed Site")
            city = str(site[2] or "Location unavailable")
            state = str(site[3] or "State unavailable")
            description = str(
                site[4] or "No description available yet."
            )

            with column:
                with st.container(border=True):

                    # Monument image
                    image_name = image_files.get(name.lower().strip())

                    if image_name:
                        image_path = IMAGE_DIR / image_name

                        if image_path.exists():
                            st.image(
                                str(image_path),
                                width='stretch'
                            )

                    # Destination number
                    st.caption(f"DESTINATION {site_index + 1:02d}")

                    # Destination name
                    st.subheader(name)

                    # Location
                    st.caption(f"📍 {city}, {state}")

                    # Short description
                    if len(description) > 160:
                        st.write(description[:160] + "...")
                    else:
                        st.write(description)

                    # Full destination details
                    with st.expander("🏛️ Explore Destination Details"):

                        st.markdown("#### About this monument")
                        st.write(description)

                        st.divider()

                        st.markdown("#### 📍 Location")
                        st.write(f"**City:** {city}")
                        st.write(f"**State:** {state}")

                        st.divider()

                                            # Historical highlights and visitor tips
                        extra = destination_info.get(name.lower().strip())

                        if extra:
                            st.markdown("#### 📜 Historical Highlights")
                            st.write(extra["history"])

                            st.markdown("**Architectural highlights**")
                            for highlight in extra["highlights"]:
                                st.markdown(f"- {highlight}")

                            st.divider()

                            st.markdown("#### 💡 Visitor Tips")
                            for tip in extra["tips"]:
                                st.markdown(f"- {tip}")

                        st.divider()

                        st.caption(f"Heritage Site ID: {site_id}")
                        st.divider()

                        if st.button(
                            "📅 Plan a Visit to This Destination",
                            key=f"plan_visit_{site_id}",
                            width="stretch"
                        ):
                            st.session_state["selected_destination"] = {
                                "id": site_id,
                                "name": name,
                                "city": city,
                                "state": state
                            }

                            st.switch_page("pages/2_Plan_Your_Visit.py")
else:
    st.info(
        "No matching heritage sites found. "
        "Try another monument name or select All States."
    )


# =====================================
# DISCOVERY FOOTER
# =====================================

st.write("")
st.divider()

render_html("""
    <div style="
        background-color: #F0EBDD;
        border-left: 4px solid #B58A45;
        border-radius: 8px;
        padding: 18px;
        margin-top: 10px;
    ">
        <div style="
            font-family: Georgia, serif;
            color: #183D2D;
            font-size: 20px;
            font-weight: bold;
        ">
            Every place has a story.
        </div>

        <div style="
            color: #68776B;
            font-size: 14px;
            margin-top: 6px;
        ">
            Explore India's heritage, understand its history
            and keep its stories alive.
        </div>
    </div>
""")

page_footer()
