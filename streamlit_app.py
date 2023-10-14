import streamlit as st

# Initialize dictionary to keep track of button presses
button_counts = {
    "Ace": 0,
    "Bullseye": 0,
    "C1 X": 0,
    "C2": 0,
    "Other": 0
}

st.title('Disc Golf Shots Tracker')

# Function to display button and update counts
def display_button(shot_type):
    if st.button(shot_type):
        button_counts[shot_type] += 1
    st.write(f"{button_counts[shot_type]}")

# Display each button
for shot_type in button_counts.keys():
    display_button(shot_type)
