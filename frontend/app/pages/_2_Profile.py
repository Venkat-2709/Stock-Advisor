import streamlit as st
import logging
from utils.api_client import start_session, reset_session
from utils.profile_client import save_profile

logger = logging.getLogger(__name__)

st.title("📊 Investment Profile Setup")

# ---------------- Session Management ----------------
if "session_id" not in st.session_state:
    st.session_state.session_id = start_session()

session_id = st.session_state.session_id
st.sidebar.success(f"Session: `{session_id}`")

if st.sidebar.button("🔁 Reset Session"):
    reset_session(session_id)
    st.session_state.clear()
    st.experimental_rerun()

# ---------------- Form ----------------
with st.form("user_profile_form"):
    risk_level = st.selectbox("Risk Level", ["Low", "Moderate", "High"])
    goal = st.selectbox("Investment Goal", ["Short Term", "Long Term"])
    sectors = st.multiselect("Preferred Sectors", [
        "Technology", "Finance", "Energy", "Healthcare", "Auto", "FMCG"
    ])

    submitted = st.form_submit_button("Save Profile")
    if submitted:
        success = save_profile(session_id, risk_level, goal, sectors)
        if success:
            logger.info(f"Profile saved successfully for session: {session_id}")
            st.success("Profile saved successfully!")
        else:
            logger.error(f"Failed to save profile for session: {session_id}")
            st.error("Failed to save profile.")
