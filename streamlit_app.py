import streamlit as st

# Custom CSS for larger buttons
st.markdown(
    """
    <style>
        .big-btn {
            font-size: 20px;
            padding: 10px 20px;
            margin: 5px;
            display: inline-block;
            background-color: #f63366;
            color: white;
            border: none;
            cursor: pointer;
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
    # Use custom HTML for larger buttons
    button_html = f'<button class="big-btn" id="{shot_type}">{shot_type}</button>'
    pressed = st.markdown(button_html, unsafe_allow_html=True)

    if st.session_state.get(shot_type, False):
        st.session_state.button_counts[shot_type] += 1
        st.session_state[shot_type] = False

    st.write(f"{st.session_state.button_counts[shot_type]}")

    # Use a script to detect button press and update session state
    st.markdown(
        f"""
        <script>
            document.getElementById("{shot_type}").onclick = function() {{
                fetch("/streamlit-v1/SessionState/{shot_type}", {{method: "POST"}});
            }};
        </script>
        """,
        unsafe_allow_html=True
    )

# Display each button
for shot_type in st.session_state.button_counts.keys():
    display_button(shot_type)
