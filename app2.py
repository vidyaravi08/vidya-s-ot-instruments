
import streamlit as st
from PIL import Image

# Data structure
equipment_data = {
    "Laryngoscope": {"explanation": "Used for visualization of the glottis.", "usage": "Check light/blade."},
    "Capnograph": {"explanation": "Monitors CO2 levels.", "usage": "Verify ETT placement."}
}

st.title("OT Equipment Navigator")
selection = st.sidebar.selectbox("Select Equipment", list(equipment_data.keys()))

st.header(selection)

# Adjustable image logic
scale = st.slider("Adjust Diagram Zoom", 0.5, 2.0, 1.0)
base_width = 400
dynamic_width = int(base_width * scale)

# Using a placeholder image URL
st.image("https://via.placeholder.com/600x400", width=dynamic_width, caption=f"Diagram of {selection}")

st.subheader("Explanation")
st.write(equipment_data[selection]["explanation"])
