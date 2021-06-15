import yfinance as yf
import streamlit as st
from datetime import datetime

today=datetime.today().strftime('%Y-%m-%d')


st.write("""
# Simple Stock Price App

Shown below are visualisations of the opening price, closing price, and the volume of the company of your choice!

         
         """)
         
options = ["GOOGL","AAPL","TSLA","AMZN"]

user_input = st.text_input("Enter in a company's ticker code (e.g. Amazon is AMZN):")

tickerSymbol = user_input
#Get data on the stock
tickerData = yf.Ticker(tickerSymbol)
#Get historical prices for the stock
tickerDf = tickerData.history(period="1d", start="2010-6-14", end=today)

st.write("""
## Opening Price 
         """)
st.line_chart(tickerDf.Open)

st.write("""
## Closing Price 
         """)
st.line_chart(tickerDf.Close)

st.write("""
## Volume
         """)
st.line_chart(tickerDf.Volume)
