# Name: Win Moe Oo
# Admin Number: 2334369
# Class: DIT/FT/3A/51

import warnings
import streamlit as st
from components.mood_gifs import get_mood_gif
from components.sidebar import render_sidebar
from helpers.theme_helper import init_theme
from components.mood_input import get_user_mood
from components.recommendations import show_recommendations
from helpers.youtube_helper import search_youtube
from helpers.mood_history_helper import save_mood_entry

warnings.filterwarnings("ignore", category=DeprecationWarning)

st.set_page_config(page_title="Home", page_icon="🏠")

# Apply theme + sidebar
init_theme()
render_sidebar()

st.title("Mood Detector App 😊")

final_mood, user_input, input_method = get_user_mood()

st.markdown("### 🎵 Recommended Song for You")

if final_mood != "unknown":
    get_mood_gif(final_mood)
    search_query = (
        f'{final_mood} music playlist for when you feel "{user_input}"'
        if input_method == "Type my feeling"
        else f"{final_mood} song official audio lyrics"
    )
    video_title, recommended_song = search_youtube(search_query)
    show_recommendations(video_title, recommended_song)
    save_mood_entry(final_mood, video_title, recommended_song)
else:
    st.write("Tell me how you feel to get a song recommendation!")
