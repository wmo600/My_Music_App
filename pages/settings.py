import streamlit as st
from components.sidebar import render_sidebar
from helpers.theme_helper import init_theme_selector

st.set_page_config(page_title="Settings", page_icon="⚙️")
init_theme_selector()   # <-- This applies and displays the theme selector

render_sidebar()
