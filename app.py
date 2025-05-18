import streamlit as st
from components.audio_input import get_voice_input
from components.tts import speak_text
from components.ocr_utils import extract_text_from_image
from utils.ai_response import get_ai_response
from utils.step_generator import structure_steps

st.set_page_config(page_title="IT Support Chatbot", layout="centered")



st.title("💬 IT Support Chatbot")
st.write("Welcome to your AI IT Assistant. Ask your tech problems!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input area
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("Type your issue:", "")
with col2:
    if st.button("🎤 Speak"):
        user_input = get_voice_input()

uploaded_file = st.file_uploader("📸 Upload Screenshot", type=["jpg", "png", "jpeg"])
if uploaded_file:
    extracted_text = extract_text_from_image(uploaded_file)
    if extracted_text:
        st.success("Text extracted from image:")
        st.write(extracted_text)
        user_input += " " + extracted_text

if user_input:
    # Add user input to history
    st.session_state.messages.append(("user", user_input))
    
    # AI response
    response = get_ai_response(user_input)
    stepwise_response = structure_steps(response)

    st.session_state.messages.append(("bot", stepwise_response))

# Display chat
for sender, msg in st.session_state.messages:
    with st.chat_message("🧑" if sender == "user" else "🤖"):
        st.markdown(msg)
        if sender == "bot":
            col1, col2 = st.columns([1, 1])
            with col1:
                st.button("🔊 Listen", on_click=lambda: speak_text(msg), key=msg)
            with col2:
                st.code(msg, language="markdown")


