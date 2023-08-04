from connection import KaggleConnection
import streamlit as st


st.set_page_config(page_title="Streamlit Connection Demo App - Kaggle Data")

st.title("Streamlit Connector Demo")
st.subheader("Top 10000 Songs on Spotify 1960-Now")

# load data
conn = st.experimental_connection("kaggle_datasets", type=KaggleConnection)
df = conn.get(path='joebeachcapital/top-10000-spotify-songs-1960-now', filename='top_10000_1960-now.csv', ttl=3600)

st.write(df.columns)

st.dataframe(df.head(20))