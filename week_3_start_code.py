import streamlit as st
import random
from googleapiclient.discovery import build
from dotenv import load_dotenv
import requests
import os

load_dotenv()
VIBEFY_READ_TOKEN = os.getenv("VIBEFY_READ_TOKEN")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def search_youtube(query, api_key=YOUTUBE_API_KEY):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=10,
        type="video",
        videoCategoryId="10",  # Category ID for Music
        videoEmbeddable="true",  # Ensure the video is embeddable
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


def get_emotion_label(text):
    API_URL = "https://router.huggingface.co/hf-inference/models/j-hartmann/emotion-english-distilroberta-base"
    headers = {
        "Authorization": f"Bearer {VIBEFY_READ_TOKEN}",
    }
    response = requests.post(API_URL, headers=headers, json={"inputs": text})

    try:
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            top_label = result[0][0]["label"].lower()
            return top_label
    except Exception as e:
        st.error("Error from Hugging Face API: ")
        print(e)


# Step 3: UI input
st.title("Mood Detector App 😊")


input_method = st.radio(
    "How do you want to share your mood?", ("Type my feeling", "Select from dropdown")
)

final_mood = "unknown"
keyword_mood = "unknown"
sentiment_based_mood = "unknown"

if input_method == "Type my feeling":
    user_input = st.text_input("How are you feeling today? (Type your feeling)")
    if user_input:
        results = get_emotion_label(user_input)
        if results:
            final_mood = results
        else:
            final_mood = "unknown"

# elif input_method == "Select from dropdown":
#     mood_option = st.selectbox("Select your mood:", ["Choose...", "joy", "sadness", "anger", "surprise", "fear", "disgust", "neutral"])
#     if mood_option != "Choose...":
#         final_mood = mood_option


# # Emojis
# mood_emojis = {
#     "joy": "😄",
#     "sadness": "😢",
#     "anger": "😡",
#     "surprise": "😲",
#     "fear": "😨",
#     "disgust": "🤢",
#     "neutral": "😐",
#     "unknown": "❓"
# }

# st.subheader(f"Final Detected Mood: {final_mood.capitalize()} {mood_emojis.get(final_mood, '')}")

# # Updated suggestions with multiple options
# suggestions = {
#     "joy": [
#         "Enjoy your day and spread the positivity! 🌟",
#         "Keep smiling and live life to the fullest!",
#         "You're awesome, keep up the good work!"
#     ],
#     "sadness": [
#         "Take care! Things will get better 💛",
#         "Sending virtual hugs — you're not alone.",
#         "You're stronger than you think. Don't give up!"
#     ],
#     "anger": [
#         "Take a deep breath. You got this. 💨",
#         "Step away and reset.",
#         "Channel your energy into something positive."
#     ],
#     "surprise": [
#         "Whoa! That was unexpected! 😲",
#         "Hope it's a good surprise!",
#         "Sometimes surprises lead to the best memories."
#     ],
#     "fear": [
#         "It's okay to feel scared — you're not alone.",
#         "Breathe through the fear, you've got this. 💪",
#         "Face it slowly, one step at a time."
#     ],
#     "disgust": [
#         "Yikes! That doesn’t sound pleasant 🤢",
#         "Let it out, sometimes things just stink.",
#         "Walk away and reset your vibe."
#     ],
#     "neutral": [
#         "Nothing wrong with an average day. 🌤️",
#         "Sometimes being 'okay' is perfectly fine.",
#         "A quiet moment is a good moment too."
#     ]
# }

# # Choose one random suggestion
# msg_list = suggestions.get(final_mood, ["Tell me more."])
# random_message = random.choice(msg_list)

# st.write(random_message)


st.markdown("### 🎵 Recommended Song for You")

if final_mood != "unknown":
    if input_method == "Type my feeling":
        search_query = f'{final_mood} music playlist for when you feel "{user_input}"'
    else:
        search_query = f"{final_mood} song official audio lyrics"
    video_title, recommended_song = search_youtube(search_query)

    if recommended_song:
        st.markdown(f"#### Video Name: [{video_title}]({recommended_song})")
        st.video(recommended_song)
    else:
        st.write("Tell me how you feel to get a song recommendation!")
