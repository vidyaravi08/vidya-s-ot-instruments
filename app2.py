
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title("3D OT Instrument Explorer")

# 1. 3D Model Logic (Example: Sphere representing an instrument tip)
def get_3d_model():
    phi = np.linspace(0, 2*np.pi, 20)
    theta = np.linspace(0, np.pi, 20)
    phi, theta = np.meshgrid(phi, theta)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z

x, y, z = get_3d_model()

# 2. Plotting the 3D figure
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
fig.update_layout(title='3D Laryngoscope Blade Model', autosize=False,
                  width=500, height=500, margin=dict(l=65, r=50, b=65, t=90))

# 3. Display in Streamlit
st.plotly_chart(fig)

# 4. Expert Clinical Explanation
st.subheader("Clinical Importance")
st.write("""
The 3D visualization allows trainees to inspect the curvature of the blade, 
which is critical for displacing the tongue and visualizing the glottis. 
Understanding the 3D geometry helps in preventing dental trauma and 
optimizing the angle of the laryngoscope during intubation.
""")
