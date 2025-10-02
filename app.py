import streamlit as st
import pandas as pd

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 135,
    "AMZN": 140,
    "MSFT": 320
}

# Page setup
st.set_page_config(page_title="Stock Portfolio Tracker", page_icon="📈")

# Title
st.title("📈 Stock Portfolio Tracker")

# Show available stocks
st.subheader("Available Stocks and Prices")
for stock, price in stock_prices.items():
    st.write(f"{stock} : ${price} per share")

# Initialize portfolio in session state
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}

# Input section
st.subheader("Add Stocks to Your Portfolio")
col1, col2 = st.columns(2)
with col1:
    stock_input = st.text_input("Stock Symbol (e.g., AAPL)").upper()
with col2:
    qty_input = st.number_input("Quantity", min_value=1, step=1)

# Add stock button
if st.button("Add Stock"):
    if stock_input not in stock_prices:
        st.warning("⚠️ Stock not found! Choose from the available stocks.")
    else:
        st.session_state.portfolio[stock_input] = st.session_state.portfolio.get(stock_input, 0) + qty_input
        st.success(f"Added {qty_input} shares of {stock_input} to portfolio!")

# Display portfolio
if st.session_state.portfolio:
    st.subheader("💼 Your Portfolio Summary")
    portfolio_data = []
    total_investment = 0
    for stock, qty in st.session_state.portfolio.items():
        price = stock_prices[stock]
        total = price * qty
        total_investment += total
        portfolio_data.append({
            "Stock": stock,
            "Quantity": qty,
            "Price per Share": price,
            "Total Value": total
        })

    df = pd.DataFrame(portfolio_data)
    st.dataframe(df)
    st.write(f"**Total Investment Value: ${total_investment}**")

    # Download portfolio as CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Download Portfolio as CSV",
        data=csv,
        file_name='portfolio_summary.csv',
        mime='text/csv'
    )
