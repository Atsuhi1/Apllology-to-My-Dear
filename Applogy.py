import streamlit as st
import time

st.set_page_config(page_title="Apology to Shiwani ❤️", page_icon="💌", layout="centered")

# Floating hearts animation
st.markdown("""
<style>
.heart {
  position: fixed;
  width: 20px;
  height: 20px;
  background-color: red;
  transform: rotate(45deg);
  animation: float 8s infinite ease-in;
  z-index: 9999;
}
.heart::before, .heart::after {
  content: "";
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: red;
  border-radius: 50%;
}
.heart::before {
  top: -10px;
  left: 0;
}
.heart::after {
  left: -10px;
  top: 0;
}
@keyframes float {
  0% {transform: translateY(100vh) rotate(45deg);}
  100% {transform: translateY(-10vh) rotate(45deg);}
}
</style>

<script>
const numHearts = 30;
for (let i = 0; i < numHearts; i++) {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDelay = Math.random() * 8 + "s";
    heart.style.opacity = Math.random();
    heart.style.transform = "scale(" + (Math.random() * 0.7 + 0.3) + ")";
    document.body.appendChild(heart);
}
</script>
""", unsafe_allow_html=True)

# Typing animation
def type_writer(message, delay=0.02):
    placeholder = st.empty()
    typed_text = ""
    for char in message:
        typed_text += char
        placeholder.markdown(typed_text, unsafe_allow_html=True)
        time.sleep(delay)

# Title
st.markdown("<h1 style='text-align: center;'>💖 A Personal Apology to Shiwani 💖</h1>", unsafe_allow_html=True)

# Button and message
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

