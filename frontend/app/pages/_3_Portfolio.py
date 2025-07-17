import streamlit as st
import logging 
from utils.portfolio_client import add_stock, get_portfolio

logger = logging.getLogger(__name__)

st.title("📈 Portfolio Manager")

session_id = st.session_state.get("session_id")
if not session_id:
    st.warning("Please set up your session from the Profile tab first.")
    st.stop()

# ---------------- Portfolio Entry ----------------
with st.form("portfolio_form"):
    symbol = st.text_input("Stock Symbol", placeholder="e.g. RELIANCE or AAPL")
    quantity = st.number_input("Quantity", step=1.0, min_value=0.0)
    buy_price = st.number_input("Buy Price", step=0.1, min_value=0.0)
    exchange = st.selectbox("Exchange", ["NSE", "BSE", "NASDAQ", "NYSE", "MF"])
    notes = st.text_area("Notes", placeholder="Optional")

    submitted = st.form_submit_button("Add to Portfolio")
    if submitted:
        success = add_stock(session_id, symbol, quantity, buy_price, exchange, notes)
        if success:
            logger.info(f"Added stock: {symbol.upper()} to portfolio.")
            st.success(f"✅ {symbol.upper()} added.")
        else:
            logger.error(f"Failed to add stock: {symbol.upper()} to portfolio.")
            st.error("❌ Failed to add.")

# ---------------- View Portfolio ----------------
st.subheader("📊 Your Portfolio")

portfolio = get_portfolio(session_id)
if portfolio:
    st.table(portfolio)
else:
    st.info("No portfolio data yet.")
