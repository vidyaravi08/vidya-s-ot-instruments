import streamlit as st

# Data structure: Define your equipment
equipment_data = {
    "Laryngoscope": {
        "explanation": "Used for visualization of the glottis during endotracheal intubation.",
        "usage": "Check light source and blade integrity before use."
    },
    "Capnograph": {
        "explanation": "Monitors CO2 levels in exhaled breath to verify ETT placement.",
        "usage": "Standard of care for confirming proper tube positioning."
    }
}

st.title("OT Equipment & Instrument Navigator")

# Sidebar navigation
selection = st.sidebar.selectbox("Select Equipment", list(equipment_data.keys()))

# Main display
st.header(selection)

# Placeholder for diagrams
# Replace 'path/to/diagram.png' with your actual image files
st.image("https://via.placeholder.com/600x400", caption=f"Diagram of {selection}")

st.subheader("Explanation")
st.write(equipment_data[selection]["explanation"])

st.subheader("Clinical Usage")
st.write(equipment_data[selection]["usage"])

# Interactive slider for "adjustability" simulation
scale = st.slider("Adjust Diagram Zoom", 0.5, 2.0, 1.0)
st.write(f"Current Diagram Zoom Scale: {scale}x"
