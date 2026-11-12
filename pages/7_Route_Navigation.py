
import streamlit as st

from components import setup_page, page_footer

from navigation import (
    haversine_distance,
    calculate_bearing,
    compass_direction,
    walking_time
)


# Setup page
setup_page("Route Navigation")


st.title("🧭 Route Navigation")

st.caption(
    "Calculate distance and direction between two locations."
)

st.divider()


# Introduction
st.subheader("Enter Location Coordinates")

st.info(
    "Enter the latitude and longitude of your starting "
    "and destination locations."
)


# Route form
with st.form("route_form"):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📍 Starting Location")

        start_lat = st.number_input(
            "Starting Latitude",
            min_value=-90.0,
            max_value=90.0,
            value=27.1751,
            format="%.6f"
        )

        start_lon = st.number_input(
            "Starting Longitude",
            min_value=-180.0,
            max_value=180.0,
            value=78.0421,
            format="%.6f"
        )

    with col2:

        st.subheader("🏁 Destination")

        end_lat = st.number_input(
            "Destination Latitude",
            min_value=-90.0,
            max_value=90.0,
            value=28.6562,
            format="%.6f"
        )

        end_lon = st.number_input(
            "Destination Longitude",
            min_value=-180.0,
            max_value=180.0,
            value=77.2410,
            format="%.6f"
        )

    calculate = st.form_submit_button(
        "Calculate Route",
        use_container_width=True
    )


# Calculate results
if calculate:

    try:

        # Check whether locations are different
        if start_lat == end_lat and start_lon == end_lon:

            st.warning(
                "Starting location and destination are the same."
            )

        else:

            # Calculate distance
            distance = haversine_distance(
                start_lat,
                start_lon,
                end_lat,
                end_lon
            )

            # Calculate bearing
            bearing = calculate_bearing(
                start_lat,
                start_lon,
                end_lat,
                end_lon
            )

            # Find direction
            direction = compass_direction(bearing)

            # Calculate walking time
            time = walking_time(distance)

            # Display results
            st.divider()
            st.subheader("🧭 Route Results")

            col1, col2 = st.columns(2)

            col1.metric(
                "Distance",
                f"{distance:.2f} km"
            )

            col2.metric(
                "Bearing",
                f"{bearing:.2f}°"
            )

            col3, col4 = st.columns(2)

            col3.metric(
                "Direction",
                direction
            )

            col4.metric(
                "Walking Time",
                f"{time:.0f} minutes"
            )

            # Display map
            import pandas as pd

            map_data = pd.DataFrame({
                "latitude": [start_lat, end_lat],
                "longitude": [start_lon, end_lon]
            })

            st.subheader("🗺️ Route Map")

            st.map(
                map_data,
                latitude="latitude",
                longitude="longitude"
            )

    except Exception as e:

        st.error(
            "Something went wrong while calculating the route."
        )

        st.exception(e)


st.divider()

st.subheader("How to find GPS coordinates?")

st.markdown("""
1. Open Google Maps.
2. Search for your heritage location.
3. Right-click on the location.
4. Click the displayed coordinates to copy them.
5. Paste latitude and longitude into the fields above.
""")

page_footer()
