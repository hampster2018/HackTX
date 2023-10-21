import streamlit as st
import pandas as pd
import plotly

st.write("# Hello World!")

conn = st.experimental_connection("db", type="sql")

with conn.session as s:
    st.write(s.execute("SELECT * FROM users").fetchall())
