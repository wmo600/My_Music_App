import streamlit as st
from components.sidebar import render_sidebar
from helpers.theme_helper import init_theme
from components.mood_history_view import show_mood_chart, show_mood_table

st.set_page_config(page_title="Mood History", page_icon="📈")
init_theme()
render_sidebar()

st.title("📈 Mood History")

show_mood_chart()

if "mh_page" not in st.session_state:
    st.session_state["mh_page"] = 1

show_mood_table(st.session_state["mh_page"])
