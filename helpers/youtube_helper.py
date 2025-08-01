# Name: Win Moe Oo
# Admin Number: 2334369
# Class: DIT/FT/3A/51
import random
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def search_youtube(query, api_key=YOUTUBE_API_KEY):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=10,
        type="video",
        videoCategoryId="10",
        videoEmbeddable="true",
    )
    response = request.execute()
    videos = response.get("items", [])
    if videos:
        selected_video = random.choice(videos)
        video_id = selected_video["id"]["videoId"]
        video_title = selected_video["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_title, video_url
    else:
        return None, None
