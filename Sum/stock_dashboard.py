import streamlit as st
import yfinance as yf
import datetime

st.title("Simple Stock Checker")
symbol = st.text_input("Enter stock symbol", "AAPL")
days = st.slider("Days to display", 1, 365, 30)

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=days)

ticker = yf.Ticker(symbol)
data = ticker.history(start=start_date, end=end_date)

if not data.empty:
    st.line_chart(data['Close'])
    st.write(f"Current price: ${data['Close'][-1]:.2f}")
else:
    st.error("No data available for this symbol")