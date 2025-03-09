import time
import streamlit as st
from datetime import datetime, timedelta

def main():
    st.title("Countdown Timer")

    # User input for countdown time
    minutes = st.number_input("Set Timer (minutes)", min_value=0, max_value=60, value=1, step=1)
    seconds = st.number_input("Set Timer (seconds)", min_value=0, max_value=59, value=0, step=1)
    
    total_seconds = int(minutes * 60 + seconds)

    # Initialize session state for countdown
    if "countdown" not in st.session_state:
        st.session_state.countdown = None

    if st.button("Start Countdown"):
        st.session_state.countdown = total_seconds  # Store countdown in session state

    # Countdown display logic
    if st.session_state.countdown is not None:
        countdown_placeholder = st.empty()  # Create a placeholder for updating countdown
        
        while st.session_state.countdown > 0:
            mins, secs = divmod(st.session_state.countdown, 60)
            countdown_placeholder.metric(label="Time Left", value=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            st.session_state.countdown -= 1
            st.rerun()  # Refresh the app dynamically

        st.session_state.countdown = None  # Reset countdown after finishing
        st.success("Time's up!")

if __name__ == "__main__":
    main()

st.write("------------------")
st.write('Made by Isha Khan')




