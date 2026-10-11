import streamlit as st
import streamlit_geolocation
import time

st.set_page_config(
    page_title="Speed Safety Alert mayank",
    page_icon="🚗",
    layout="centered"
)

SPEED_LIMIT = 60

st.title("🚗 Speed Safety Alert")
st.write("Drive Safe. Protect Your Family.")

st.info(f"Speed Limit: {SPEED_LIMIT} km/h")

st.subheader("📍 GPS Location")

location = streamlit_geolocation.streamlit_geolocation()

if location and location.get("latitude") is not None:
    st.success("GPS Location Received!")

    st.write("Latitude:", location["latitude"])
    st.write("Longitude:", location["longitude"])

    st.info(
        "GPS location mil gayi hai. "
        "Actual speed calculate karne ke liye "
        "multiple GPS readings chahiye."
    )
else:
    st.warning(
        "Location abhi nahi mili. "
        "Browser mein location permission allow karo."
    )

st.divider()

st.subheader("🧪 Speed Test")

speed = st.number_input(
    "Enter speed (km/h)",
    min_value=0.0,
    max_value=300.0,
    value=40.0,
    step=1.0
)

if st.button("Check Speed"):
    if speed > SPEED_LIMIT:
        st.error("🚨 OVERSPEED ALERT!")
        st.write(f"Speed: {speed} km/h")
        st.warning("Please slow down safely.")
    else:
        st.success("✅ SAFE SPEED")
        st.write(f"Speed: {speed} km/h")

st.caption("Speed Safety Alert | Prototype")