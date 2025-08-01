import streamlit as st
import pathlib
from streamlit_cookies_manager import CookieManager


cookie_manager = CookieManager()
cookie_manager._get_cookies()


def get_assets_path():
    return pathlib.Path(__file__).parent.parent / "assets" / "styles"


def get_available_themes():
    styles_path = get_assets_path()
    return [p.stem for p in styles_path.glob("*.css")]


def apply_theme(theme_name: str):
    css_path = get_assets_path() / f"{theme_name}.css"
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def init_theme():
    themes = get_available_themes()
    default_theme = (
        "light_theme" if "light_theme" in themes else (themes[0] if themes else None)
    )

    # Try to load theme from cookie
    theme_from_cookie = cookie_manager.get("theme")
    theme_valid = theme_from_cookie in themes

    # Only set session theme if missing/invalid, and sync with cookie
    if "theme" not in st.session_state or st.session_state["theme"] not in themes:
        st.session_state["theme"] = theme_from_cookie if theme_valid else default_theme

    if st.session_state["theme"]:
        apply_theme(st.session_state["theme"])
        # Always sync cookie to latest value
        cookie_manager.__setitem__("theme", st.session_state["theme"])


def init_theme_selector():
    themes = get_available_themes()
    theme_display_names = {t: t.replace("_", " ").title() for t in themes}

    init_theme()

    def update_theme():
        apply_theme(st.session_state["theme"])
        # Also set cookie so refresh remembers it
        cookie_manager.__setitem__("theme", st.session_state["theme"])

    st.selectbox(
        "Choose a Theme:",
        options=themes,
        format_func=lambda t: theme_display_names[t],
        index=themes.index(st.session_state["theme"]),
        key="theme",
        on_change=update_theme,
    )
