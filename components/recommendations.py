# Name: Win Moe Oo
# Admin Number: 2334369
# Class: DIT/FT/3A/51
import streamlit as st


def show_recommendations(video_title, recommended_song):

    if recommended_song:
        st.markdown(f"#### Video Name: [{video_title}]({recommended_song})")
        st.video(recommended_song)
    else:
        st.write("Couldn't find a video right now. Try again!")
