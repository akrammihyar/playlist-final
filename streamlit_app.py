import pandas as pd
import streamlit as st

st.markdown("""# Quiz night?
pick from the following list

""")

df = pd.read_csv("playlists.csv")
years = list(range(1, 12))

year_list = st.multiselect(label="Start Year", options=years, default= [1, 2])


if st.button('Play'):
    if len(year_list) == 1:
        playlist_name = f"Card: {year_list[0]}"
    else:
        playlist_name = f"Card: {year_list[0]}-{year_list[1]}"

    if df[df['name'] == playlist_name].shape[0] > 0:
        playlist = df[df['name'] == playlist_name].to_dict(orient='records')[0]
    else:
        playlist = "Ooops, it looks like we didn't make that playlist yet. Playlists with a range of 1-20 years were created. Try again with a more narrow year range."

    if isinstance(playlist, dict):
        link = f"### Your Spotify Playlist: [{playlist['name']}]({playlist['link']})"
        st.markdown(link, unsafe_allow_html=True)
    else:
        st.markdown(playlist)
