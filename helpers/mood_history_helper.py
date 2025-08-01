# Name: Win Moe Oo
# Admin Number: 2334369
# Class: DIT/FT/3A/51
import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path("data/mood_history.json")


def load_mood_history():
    if not HISTORY_FILE.exists():
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_mood_entry(mood, video_title, video_url):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mood": mood,
        "video_title": video_title,
        "video_url": video_url,
    }
    data = load_mood_history()
    data.append(entry)
    HISTORY_FILE.parent.mkdir(exist_ok=True)
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_paginated_history(page=1, per_page=10):
    data = load_mood_history()
    data = sorted(data, key=lambda x: x["timestamp"], reverse=True)
    total_pages = max(1, len(data) // per_page + int(len(data) % per_page != 0))
    start = (page - 1) * per_page
    end = start + per_page
    return data[start:end], total_pages
