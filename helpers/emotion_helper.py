# Name: Win Moe Oo
# Admin Number: 2334369
# Class: DIT/FT/3A/51
import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
VIBEFY_READ_TOKEN = os.getenv("VIBEFY_READ_TOKEN")


def get_emotion_label(text):
    API_URL = "https://router.huggingface.co/hf-inference/models/j-hartmann/emotion-english-distilroberta-base"
    headers = {
        "Authorization": f"Bearer {VIBEFY_READ_TOKEN}",
    }
    response = requests.post(API_URL, headers=headers, json={"inputs": text})

    try:
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0][0]["label"].lower()
    except Exception as e:
        st.error("Error from Hugging Face API")
        print(e)
    return "unknown"
