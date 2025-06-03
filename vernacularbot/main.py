import streamlit as st
from googletrans import Translator
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

translator = Translator()

LANGUAGES = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Marathi": "mr"
}


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Hindi"

 
st.title("Chat smart. Speak native. 🗣️")

selected_language = st.selectbox(
    "Choose your preferred language:",
    list(LANGUAGES.keys()),
    index=list(LANGUAGES.keys()).index(st.session_state.selected_language)
)
st.session_state.selected_language = selected_language
target_lang_code = LANGUAGES[selected_language]



user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    try:
        translated_input = translator.translate(user_input, dest='en').text
        response = openai.ChatCompletion.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that replies clearly and politely."},
                {"role": "user", "content": translated_input}
            ]
        )

        llm_reply = response.choices[0].message.content
        translated_reply = translator.translate(llm_reply, dest=target_lang_code).text
        st.session_state.chat_history.append({
            "user": user_input,
            "bot": translated_reply
        })
        st.rerun()

    except Exception as e:
        st.error(f"Error: {e}")
st.subheader("📝 Chat History")
for chat in st.session_state.chat_history:
    st.markdown(f"**👤 You:** {chat['user']}")
    st.markdown(f"**🤖 Bot:** {chat['bot']}")

if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()