import streamlit as st
import requests
import  json
import pandas as pd
st.title('Dashboard')



@st.cache_data
def load_data():
	r = requests.get(f"{BASE_URL}/api/v1/query_range", params={
		'query': '{__name__=\"kraken__doge_usdt_bid_price\"}',
		'start': 1708904080000,
		'end': 1709506900000
	})
	d = r.json()
	return d

d = load_data()

st.title("JSON data")
st.json(d)



name = d['data']['result'][0]['metric']['__name__']
asset = d['data']['result'][0]['metric']['asset']
exchange = d['data']['result'][0]['metric']['exchange']


st.title(f"DataFrame: {name}")

df = pd.DataFrame(d['data']['result'][0]['values'], columns=["date", "value"])

df['date']= pd.to_datetime(df['date'], unit='s')


st.dataframe(df)
