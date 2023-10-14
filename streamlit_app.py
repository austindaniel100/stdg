import streamlit as st

# Custom CSS for larger buttons
st.markdown(
    """
    <style>
        .big-btn {
            font-size: 20px;
            padding: 10px 20px;
            margin: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Check if 'button_counts' is already in the session state
if 'button_counts' not in st.session_state:
    st.session_state.button_counts = {
        "Ace": 0,
        "Bullseye": 0,
        "C1 X": 0,
        "C2": 0,
        "Other": 0
    }

st.title('Disc Golf Shots Tracker')

# Function to display button and update counts
def display_button(shot_type):
    # Use custom CSS class for larger buttons
    if st.button(shot_type, key=shot_type, class_name="big-btn"):
        st.session_state.button_counts[shot_type] += 1
    st.write(f"{st.session_state.button_counts[shot_type]}")

# Display each button
for shot_type in st.session_state.button_counts.keys():
    display_button(shot_type)
