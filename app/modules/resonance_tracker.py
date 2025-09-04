import streamlit as st
import pandas as pd
import os

# --- Load or Create Data ---
DATA_PATH = os.path.join("data", "resonance_events.csv")

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
else:
    df = pd.DataFrame(columns=["Timestamp", "Event", "Emotion", "Resonance Score"])

# --- UI ---
st.header("🎼 Resonance Tracker")
st.markdown("Log emotional events, tag frequencies, and track your harmonic journey.")

# --- Input Form ---
with st.form("log_event"):
    event = st.text_input("Event Description")
    emotion = st.selectbox("Emotional Frequency", [
        "Heartbreak", "Empathy", "Awe", "Nostalgia", "Clarity", "Urgency", "Peace"
    ])
    score = st.slider("Resonance Score", 0, 100, 50)
    submitted = st.form_submit_button("Log Event")

    if submitted and event:
        new_entry = {
            "Timestamp": pd.Timestamp.now(),
            "Event": event,
            "Emotion": emotion,
            "Resonance Score": score
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)
        st.success("Event logged successfully!")

# --- Display Logged Events ---
st.markdown("### 🔍 Logged Events")
st.dataframe(df)
