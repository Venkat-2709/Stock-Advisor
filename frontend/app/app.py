import streamlit as st
import logging
from .frontend_logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

logger.info("Streamlit app started.")

st.set_page_config(page_title="Stock Advisor", layout="wide")

st.title("🧠 Stock Advisor")

tabs = st.tabs(["📊 Dashboard", "👤 Profile", "💼 Portfolio"])

with tabs[0]:
    from pages._1_Dashboard import show_dashboard
    show_dashboard()

with tabs[1]:
    from pages._2_Profile import show_profile
    show_profile()

with tabs[2]:
    from pages._3_Portfolio import show_portfolio
    show_portfolio()
