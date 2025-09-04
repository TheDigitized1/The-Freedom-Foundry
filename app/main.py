import streamlit as st

st.set_page_config(page_title="Freedom Foundry", page_icon="🛠️", layout="centered")
st.title("🛠️ The Freedom Foundry")
st.write("If you're seeing this, the app is working!")


# --- Page Config ---
st.set_page_config(
    page_title="The Freedom Foundry",
    page_icon="🛠️",
    layout="centered"
)

# --- Header ---
st.title("🛠️ The Freedom Foundry")
st.markdown("### Where Strategy Meets Soul")

# --- Purpose ---
st.markdown("""
Welcome to The Freedom Foundry—a living system for builders, seekers, and emotional architects.
This space is designed to harmonize logic, intuition, and creative mastery.
""")

# --- Goals ---
st.markdown("#### 🔍 Core Goals")
st.markdown("""
- **Strategic Mastery**: Build scoring systems and decision frameworks  
- **Emotional Intelligence**: Track resonance events, harmonics, and vibe shifts  
- **Creative Expression**: Storyboard timelines and prototype ideas  
- **Sustainable Design**: Source ethical materials and modular accessories  
- **Community Curation**: Vet aligned thinkers and build a signal-based network
""")

# --- Current Projects ---
st.markdown("#### ⚙️ Current Projects")
projects = {
    "Resonance Tracker": "Emotional frequency logging system with dual-mode views",
    "Real Estate Intelligence": "Scoring matrix for lifestyle-aligned land acquisition",
    "Disaster Preparedness Planner": "Modular supply tracker + scenario simulator",
    "Harmonic Mapper": "Tool to visualize layered emotional frequencies",
    "Modular Workspace Builder": "Bamboo + magnetic accessory prototyping",
    "Carlos Santana Mastery Archive": "Storytelling collage honoring creative excellence"
}

for name, desc in projects.items():
    st.markdown(f"**{name}** — {desc}")

Add minimal UI block to test Streamlit rendering

# --- Footer Quote ---
st.markdown("---")
st.markdown("> “You’re not just building a dashboard. You’re composing a symphony of self-awareness.”")

#import modules.resonance_tracker as rt

st.markdown("---")
st.markdown("### 🔗 Modules")
if st.button("Open Resonance Tracker"):
    rt
