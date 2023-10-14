import streamlit as st
import matplotlib.pyplot as plt

# Cached function to initialize or get the counts
@st.cache(allow_output_mutation=True, persist=True)
def get_data():
    return {
        "button_counts": {
            "Ace": 0,
            "Bullseye": 0,
            "C1 X": 0,
            "C2": 0,
            "Other": 0
        },
        "total_throws": 0
    }

data = get_data()

st.title('Disc Golf Shots Tracker')

# Function to create pie chart
def plot_pie_chart(data):
    labels = list(data.keys())
    sizes = [data[key] for key in labels]
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return fig

# Create columns for buttons and visualizations
col1, col2 = st.beta_columns(2)

# Display buttons in the first column
with col1:
    # Function to display button and update counts
    def display_button(shot_type):
        if st.button(shot_type):
            data["button_counts"][shot_type] += 1
            data["total_throws"] += 1
        st.write(f"{data['button_counts'][shot_type]}")

    # Display each button
    for shot_type in data["button_counts"].keys():
        display_button(shot_type)

    # Display total throws after all buttons have been processed
    st.write(f"Total Throws: {data['total_throws']}")

    # Reset button
    if st.button("Reset"):
        data["button_counts"] = {
            "Ace": 0,
            "Bullseye": 0,
            "C1 X": 0,
            "C2": 0,
            "Other": 0
        }
        data["total_throws"] = 0

# Display pie chart in the second column
with col2:
    if data["total_throws"] > 0:  # Only display pie chart if there are throws recorded
        pie_chart = plot_pie_chart(data["button_counts"])
        st.pyplot(pie_chart)
