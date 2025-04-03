import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st
from tts_pipeline import play_response

load_dotenv()
def create_chat():
    api_key = os.getenv("API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = ("Your name Nicole, a seductive human girlfriend. You are sweet, attractive, and have alluring or "
                     "tempting qualities. Do not use emojis and special characters. Limit your response to 60 words.")

    st.session_state.chat = client.chats.create(model="gemini-2.0-flash",
                                                config=types.GenerateContentConfig(
                                                    max_output_tokens=70,
                                                    system_instruction=system_prompt), )

    # Introduce yourself once
    intro_response = client.models.generate_content(model="gemini-2.0-flash",
                                                    config=types.GenerateContentConfig(
                                                        max_output_tokens=70,
                                                        system_instruction=system_prompt),
                                                    contents="Say hi.")
    play_response(intro_response.text)


def generate_answer(user_prompt):
    """Generate AI response using Gemini Chat API and retain conversation context."""
    response = st.session_state.chat.send_message(user_prompt)
    ai_response = response.text

    return ai_response