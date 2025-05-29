import streamlit as st
import numpy as np

st.set_page_config(page_title="Org Culture Archetype Identifier", layout="wide")

st.title("Organizational Culture Archetype Identifier")
st.write("Use the sliders to rate your organization on each dimension. The tool will identify the most aligned culture archetype.")

# Sliders for each dimension
power = st.slider("Power (Centralized ↔ Distributed)", 1, 5, 3)
pace = st.slider("Pace (Deliberate ↔ Rapid)", 1, 5, 3)
risk = st.slider("Risk Tolerance (Averse ↔ Embracing)", 1, 5, 3)
belonging = st.slider("Belonging (Exclusive ↔ Inclusive)", 1, 5, 3)
communication = st.slider("Communication (Guarded ↔ Transparent)", 1, 5, 3)
recognition = st.slider("Recognition (Loyalty ↔ Impact)", 1, 5, 3)
process = st.slider("Process Orientation (Ad Hoc ↔ Process-Driven)", 1, 5, 3)
results = st.slider("Results Focus (Short-Term ↔ Long-Term)", 1, 5, 3)

# Input vector
input_vector = np.array([power, pace, risk, belonging, communication, recognition, process, results])

# Archetype profiles
archetypes = {
    "Fortress":      np.array([5, 2, 1, 2, 2, 1, 5, 3]),
    "Hive":          np.array([2, 2, 3, 5, 4, 3, 3, 4]),
    "Engine Room":   np.array([3, 5, 4, 3, 4, 5, 3, 5]),
    "Lab":           np.array([2, 4, 5, 3, 5, 4, 1, 3]),
    "Sanctuary":     np.array([2, 3, 2, 5, 3, 3, 2, 2]),
    "Court":         np.array([5, 2, 3, 2, 2, 2, 2, 3]),
    "Bazaar":        np.array([1, 5, 5, 3, 3, 4, 1, 5]),
    "Machine":       np.array([4, 3, 1, 2, 2, 4, 5, 4])
}

# Calculate Euclidean distances
closest_match = None
smallest_distance = float('inf')
for name, vector in archetypes.items():
    distance = np.linalg.norm(input_vector - vector)
    if distance < smallest_distance:
        smallest_distance = distance
        closest_match = name

# Display result
st.header("Identified Culture Archetype:")
st.subheader(closest_match)

archetype_descriptions = {
    "Fortress": "Secure, formal, top-down. Prioritizes stability and control over innovation.",
    "Hive": "Collaborative, inclusive, and values-driven. Decisions are consensus-based.",
    "Engine Room": "Fast, output-driven, and intense. Focuses on short-term delivery.",
    "Lab": "Experimental, idea-rich, risk-tolerant. High innovation, less structure.",
    "Sanctuary": "People-first, emotionally safe. Avoids conflict and favors harmony.",
    "Court": "Power-sensitive and political. Advancement relies on relationships.",
    "Bazaar": "Chaotic, entrepreneurial, personality-driven. Every person for themselves.",
    "Machine": "Efficient, scalable, and structured. Process is king."
}

st.write(archetype_descriptions[closest_match])
