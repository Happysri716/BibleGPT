import subprocess
import streamlit as st

if "history" not in st.session_state:
    st.session_state.history = []

def ask_bible(q: str) -> str:
    prompt = "You are a Bible expert. Only answer using the Bible. " + q
    res = subprocess.run(
        ["gemini", "--prompt", prompt],
        capture_output=True,
        text=True,
        shell=True
    )
    return res.stdout.strip() if res.returncode == 0 else f"Error: {res.stderr.strip()}"

st.title("📖 BibleGPT")

# 👇 Correct tab unpacking
tab1, = st.tabs(["Chat"])

with tab1:
    chat_q = st.text_input("Ask a Bible question:", key="chat_q")
    if st.button("Ask Question", key="chat_btn"):
        if not chat_q.strip():
            st.warning("🛑 Please type a question first!")
        else:
            answer = ask_bible(chat_q)
            st.session_state.history.append((chat_q, answer))

    for user_q, bot_ans in st.session_state.history:
        st.write(f"👤 You asked: {user_q}")
        st.write(f"🤖 BibleGPT answered: {bot_ans}")
