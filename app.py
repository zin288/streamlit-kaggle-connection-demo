from connection import KaggleConnection
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Streamlit Connection Demo App - Kaggle Data")
st.title("Streamlit Connector Demo using Kaggle Dataset")

st.subheader("Connections Hackathon")
st.markdown('This is a demo app with makes use of the recent release of `st.experimental_connection` to connect to the Kaggle API for the extraction csv data.')
st.markdown('As a reference, the following code is used in `app.py`:')
code_1 = '''
conn = st.experimental_connection("kaggle_datasets", type=KaggleConnection)
df = conn.get(path='joebeachcapital/top-10000-spotify-songs-1960-now', filename='top_10000_1960-now.csv', ttl=3600)
'''
st.code(code_1, language = 'python')

# load data
conn = st.experimental_connection("kaggle_datasets", type=KaggleConnection)
df = conn.get(path='joebeachcapital/top-10000-spotify-songs-1960-now', filename='top_10000_1960-now.csv', ttl=3600)

st.subheader("Kaggle Dataset")
st.write('The top 10,000 songs on spotify from 1960 till now are extracted. Here\'s part of the the data:')
st.dataframe(df.head(5))


st.divider()


st.subheader("Do you know all of your favourite singer's songs? ")
st.write('Give it a listen!')

# Filter the DataFrame to only include songs with a preview URL
df_preview = df.dropna(subset=['Track Preview URL'])

# Allow the user to select an artist
artist_name = st.selectbox('Select an artist', df_preview['Artist Name(s)'].unique())

# Filter the DataFrame based on the selected artist
df_artist = df_preview[df_preview['Artist Name(s)'] == artist_name]

# Allow the user to select a song from the filtered DataFrame
track_name = st.selectbox('Select a song', df_artist['Track Name'].unique())

# Find the Track Preview URL for the selected song
track_preview_url = df_artist[df_artist['Track Name'] == track_name]['Track Preview URL'].values[0]

# Play the audio
st.audio(track_preview_url, format='audio/mp3')

track_image = df_artist[df_artist['Track Name'] == track_name]['Album Image URL'].values[0]
st.image(track_image, caption=artist_name, use_column_width=True)