import streamlit as st
import pandas as pd
import plotly.express as px

from utils.profile_client import get_profile
from utils.portfolio_client import get_portfolio

def show_dashboard():
    st.subheader("📊 Overview Dashboard")

    session_id = st.session_state.get("session_id")
    if not session_id:
        st.warning("No active session. Please go to 'Profile' tab to start.")
        return

    # --- Fetch Data ---
    profile = get_profile(session_id)
    portfolio = get_portfolio(session_id)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👤 Profile Summary")
        if profile:
            st.success(
                f"""
                **Risk Level**: {profile['risk_level']}  
                **Goal**: {profile['goal']}  
                **Preferred Sectors**: {', '.join(profile['preferred_sectors'])}
                """
            )
        else:
            st.error("Profile not found.")

    with col2:
        st.markdown("### 💼 Portfolio Summary")
        if portfolio:
            df = pd.DataFrame(portfolio)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No portfolio data yet.")

    # --- Charts ---
    if portfolio:
        df = pd.DataFrame(portfolio)

        # Pie chart by sector
        st.markdown("### 📊 Sector Distribution")
        fig1 = px.pie(df, names="exchange", values="quantity", title="Stock Distribution by Exchange")
        st.plotly_chart(fig1, use_container_width=True)

        # Profit/Loss bar chart (mockup logic for now)
        df["current_price"] = df["buy_price"] * 1.1  # Replace with real-time fetch later
        df["pnl"] = (df["current_price"] - df["buy_price"]) * df["quantity"]
        fig2 = px.bar(df, x="stock_symbol", y="pnl", color="pnl", title="Profit/Loss per Stock")
        st.plotly_chart(fig2, use_container_width=True)
