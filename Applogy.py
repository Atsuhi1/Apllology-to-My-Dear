import streamlit as st
import time

st.set_page_config(page_title="Apology to Shiwani ❤️", page_icon="💌", layout="centered")

def type_writer(message, delay=0.02):
    placeholder = st.empty()
    typed_text = ""
    for char in message:
        typed_text += char
        placeholder.markdown(typed_text, unsafe_allow_html=True)
        time.sleep(delay)

st.markdown("<h1 style='text-align: center;'>💖 A Personal Apology to Shiwani 💖</h1>", unsafe_allow_html=True)

if st.button("Send Apology from Arnav"):
    apology_message = """
<p style='font-size: 18px; line-height: 1.6'>
Dear Shiwani,<br><br>

I know I've let you down.  
In trying to hold on to you, I forgot to hold myself up — and in the process, I made you carry more than you ever should have.  
For that, I am deeply, achingly sorry.<br><br>

You were my calm when my mind was in chaos, my anchor when I drifted too far — and instead of cherishing you, I clung too tightly.  
You didn’t deserve to feel overwhelmed, unheard, or burdened.  
You deserved peace, laughter, and someone who lifted your spirit.  
And for not being that person... I carry a weight of regret.<br><br>

But Shiwani, I am growing. Not just for you — for us.  
I want to become someone you can turn to with ease, not caution.  
Someone who brings light into your day, not shadows of guilt or worry.<br><br>

Thank you for your patience, your kindness, and your love — even when I didn’t make it easy to give.  
If I could take back the heaviness I caused, I would a thousand times.  
But all I can do now is promise: I’m becoming better.  
For you. For us. For love that deserves more.<br><br>

With all my heart,<br>
<strong>Arnav ❤️</strong>
</p>
"""
    type_writer(apology_message)

st.markdown("<br><hr><center>Made with love by Arnav</center>", unsafe_allow_html=True)

