import streamlit as st
import pandas as pd

data = pd.read_csv("20260211realtime_zone.csv")
st.dataframe(data)
