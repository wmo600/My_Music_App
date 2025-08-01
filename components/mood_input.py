import streamlit as st
from helpers.emotion_helper import get_emotion_label


def get_user_mood():
    final_mood = "unknown"
    user_input = ""
    input_method = st.radio(
        "How do you want to share your mood?",
        ("Type my feeling", "Select from dropdown"),
    )

    if input_method == "Type my feeling":
        user_input = st.text_input("How are you feeling today? (Type your feeling)")
        if user_input:
            final_mood = get_emotion_label(user_input)

    # Dropdown method (if needed)
    elif input_method == "Select from dropdown":
        mood_option = st.selectbox("Select your mood:", ["Choose...", "anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"])
        if mood_option != "Choose...":
            final_mood = mood_option

    return final_mood, user_input, input_method
