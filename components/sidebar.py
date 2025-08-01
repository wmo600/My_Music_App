# Name: Win Moe Oo
# Admin Number: 2334369
# Class: DIT/FT/3A/51
import streamlit as st


def render_sidebar():
    # Hide default auto-generated sidebar navigation
    st.markdown(
        """
    <style>
    /* Hide default sidebar navigation and the highlight bar */
    [data-testid="stSidebarNav"],           /* Navigation links */
    [data-testid="stSidebarNavItems"],      /* Container for links */
    [data-testid="stSidebarNavLink"],       /* Each link */
    [data-testid="stSidebarNavLink"].active /* Active (highlighted) link */
    {
        display: none !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        # Logo and title
        # st.image("assets/images/logo.png", width=80)
        st.markdown("## My Music App 🎵")

        # Navigation buttons
        if st.button("🏠 Home"):
            st.switch_page("app.py")  # main page
        if st.button("⚙️ Settings"):
            st.switch_page("pages/settings.py")
        if st.button("📈 Mood History"):
            st.switch_page("pages/mood_history.py")
