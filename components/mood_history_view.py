import streamlit as st
import pandas as pd
import altair as alt
from helpers.mood_history_helper import get_paginated_history, load_mood_history


def show_mood_chart():
    history = load_mood_history()
    if not history:
        st.info("No mood history yet.")
        return

    df = pd.DataFrame(history)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    chart = (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(
            x="timestamp:T", y=alt.Y("mood:N", sort=None), tooltip=["timestamp", "mood"]
        )
        .properties(width="container", height=300, title="Mood Over Time")
    )

    st.altair_chart(chart, use_container_width=True)


def show_mood_table(page, per_page=10):
    history, total_pages = get_paginated_history(page, per_page)
    if not history:
        st.write("No history found.")
        return

    st.subheader("📋 Past Recommendations")
    for entry in history:
        st.markdown(
            f"- **{entry['timestamp']}**: {entry['mood'].title()} — "
            f"[{entry['video_title']}]({entry['video_url']})"
        )

    # Pagination control
    st.markdown("---")
    cols = st.columns(3)
    if cols[0].button("⬅️ Prev", disabled=page <= 1):
        st.session_state["mh_page"] = page - 1
    cols[1].markdown(f"**Page {page} / {total_pages}**")
    if cols[2].button("➡️ Next", disabled=page >= total_pages):
        st.session_state["mh_page"] = page + 1
