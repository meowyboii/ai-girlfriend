import streamlit as st
from chatbot import create_chat, generate_answer
from stt_pipeline import speech_to_text
from tts_pipeline import play_response

def display_convo():
    # Display conversation history
    st.subheader("💬 Conversation")
    for message in st.session_state.chat.get_history():
        role = "You" if message.role == "user" else "Nicole"
        st.write(f"**{role}:** {message.parts[0].text}")

# Initialize the chat session if not already created
if "chat" not in st.session_state:
    create_chat()

# Retrieve the chat session
chat = st.session_state.chat

st.title("💖 AI Girlfriend - Nicole 💖")

# Streamlit's built-in audio recorder
audio_file = st.audio_input("Record your voice")

if audio_file:
    # Convert audio to text
    user_input = speech_to_text(audio_file)

    # Get AI response and display conversation
    response = generate_answer(user_input)
    display_convo()

    # Output response as audio
    play_response(response)
