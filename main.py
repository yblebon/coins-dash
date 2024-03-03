import streamlit as st
import requests
import  json
st.title('Dashboard')

BASE_URL = ""


@st.cache_data
def load_data():
	r = requests.get(f"{BASE_URL}/api/v1/query_range", params={
		'query': '{__name__=\"kraken__doge_usdt_ask_price\"}',
		'start': 1708904080000,
		'end': 1709506900000
	})
	data = r.json()
	return data

load_data()