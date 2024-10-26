import streamlit as st
import pandas as pd
import time
import random

# Simulated data
disasters = [
    {"type": "Fire", "location": "Forest Zone A", "severity": "High"},
    {"type": "Flood", "location": "River Area", "severity": "Moderate"},
    {"type": "Earthquake", "location": "City Center", "severity": "Critical"},
    {"type": "Landslide", "location": "Mountain Range", "severity": "High"},
    {"type": "Storm", "location": "Coastal Area", "severity": "Moderate"},
]

# Display disaster alerts
def display_alerts():
    st.title("Disaster Response System Simulation")
    st.subheader("Disaster Alerts")
    for disaster in disasters:
        st.write(f"**Type**: {disaster['type']}, **Location**: {disaster['location']}, **Severity**: {disaster['severity']}")
    st.write("---")

# Function to simulate drone dispatch
def dispatch_drone(disaster):
    st.write(f"Dispatching drone to {disaster['location']} for {disaster['type']} response...")
    time.sleep(2)  # Simulate drone travel time
    st.success(f"Drone successfully deployed to {disaster['location']} to handle {disaster['type']}.")

# Streamlit sidebar for drone dispatch
st.sidebar.title("Drone Dispatch Center")
selected_disaster = st.sidebar.selectbox("Select Disaster", [d["type"] for d in disasters])

if st.sidebar.button("Send Drone"):
    selected = next(d for d in disasters if d["type"] == selected_disaster)
    dispatch_drone(selected)

# Display disaster alerts on the main screen
display_alerts()
