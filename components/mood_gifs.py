import streamlit as st

mood_gifs = {
    "joy": "https://i.pinimg.com/originals/f3/d7/88/f3d788f927b4076a32b12d4a31aa8637.gif",
    "anger":
    "disgust":
    "fear":
    "neutral":
    "sadness":
    "surprise":
}


def get_mood_gif(mood):
    """Returns a GIF URL based on the user's mood."""
    mood_gif = mood_gifs.get(mood, "")
    if mood_gif:
        return st.image(mood_gif, use_column_width=True)