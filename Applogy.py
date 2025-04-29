import streamlit as st
import time

st.set_page_config(page_title="Apology to Shiwani ❤️", page_icon="💌", layout="centered")

def type_writer(message):
    typed_text = ""
    for char in message:
        typed_text += char
        st.markdown(f"```{typed_text}```", unsafe_allow_html=True)
        time.sleep(0.03)

# Title and layout
st.markdown("<h1 style='text-align: center;'>💖 A Personal Apology to Shiwani 💖</h1>", unsafe_allow_html=True)

if st.button("Send Apology from Arnav"):
    apology_message = f"""
Dear Shiwani,

I'm truly sorry for being overly dependent and for putting pressure on you.
I realize now how it must have felt — overwhelming, exhausting — and I deeply regret it.
You’ve always been supportive, caring, and patient with me.

I want to grow into someone you can lean on too. Someone who's emotionally stable, thoughtful, and balanced.
Not someone who adds weight to your day, but someone who lifts it.

I’m learning to stand stronger, not just for myself — but for us.
Thank you for being in my life, for your patience, and your heart.

With love and sincerity,  
Arnav ❤️
"""
    type_writer(apology_message)

st.markdown("<br><hr><center>Made with love by Arnav</center>", unsafe_allow_html=True)
