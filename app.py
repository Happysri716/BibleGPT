import streamlit as st
import os
from google import genai

# Initialize Gemini client
os.environ["AIzaSyDR8LUu6hKvnTnZ8KvqWb6HN5MGRwQquvA"] = st.secrets["AIzaSyDR8LUu6hKvnTnZ8KvqWb6HN5MGRwQquvA"]
genai_client = genai.Client()

if "history" not in st.session_state:
    st.session_state.history = []

def ask_bible(q: str) -> str:
    prompt = "You are a Bible expert. Only answer using the Bible. " + q
    response = genai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

st.title("📘 BibleGPT")

chat_q = st.text_input("Ask a Bible question:", key="chat_q")
if st.button("Ask Question"):
    if not chat_q.strip():
        st.warning("🔴 Please type a question first!")
    else:
        answer = ask_bible(chat_q)
        st.session_state.history.append((chat_q, answer))

for user_q, ans in st.session_state.history:
    st.write(f"👤 You asked: **{user_q}**")
    st.write(f"🤖 BibleGPT answered: {ans}")
