import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon="👾", layout="centered")

def load_lottieurl1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# USe local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/app.css")

    

# --- Load assets---
lottie_pic1 = load_lottieurl1("https://assets9.lottiefiles.com/packages/lf20_7X0d6AzODk.json")
lottie_pic2 = load_lottieurl2("https://assets7.lottiefiles.com/packages/lf20_9W7N8f.json")
img_1 = Image.open("Images/cruise.png")
img_2 = Image.open("Images/mapper.png")
img_3 = Image.open("Images/dosher.png")


# ----HEADER-----
with st.container():
    st.subheader("Hi, I am Claudiu 🖐")
    st.title("Junior Software Engineer from Leeds, UK 🇬🇧")
    st.subheader("JAVASCRIPT, REACT, EXPRESS, HTML, CSS, PYTHON")
    st.write("Passionate about programming and amazed about how a few lines of code can change your life...and others 😂 ")
    st.write("[Learn more >](https://github.com/Claudiu-Petre)")
    st.markdown("")

# ----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(""" 
    
    
    I am transitioning from Site Managing into Software Development by learning and assimilating a variety of technologies through a variety of: 
    - courses,
    - tutorials,
    - boot camps, 
    - books and articles,
    - etc. 

    Also, I am looking for opportunities that would allow me full time software development experience for:
    - a comprehensive understanding of programming,
    - personal contribution to business and domestic solutions,
    - building a versatile programming style.
        """)

    with right_column:
        st_lottie(lottie_pic1, height=600, key="coding")

# --- Projects---

with st.container():
    st.write("---")
    st.header("Projects... just a few")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
       st.image(img_1)
    with text_column:
        st.subheader("A Javascript project that exploits the Object Oriented Programming concepts")
        st.write(
            """Learn how to navigate using Cruise ships GUI""")        
        st.markdown("[Find it here...](https://github.com/Claudiu-Petre/Cruise-ships)")

st.write("---")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader('"Leaflet" - a geolocation library in JS')
        st.write("""Learn how to track your favorite sports using Mapper""")
        st.markdown('[Find it here...](https://github.com/Claudiu-Petre/mapper)')

st.write("---")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_3)
    with text_column:
        st.subheader('Objects, DOM manipulation, Functions and Arrays in JS')
        st.write("""Manage your finances with Do$her""")
        st.markdown('[Find it here...](https://github.com/Claudiu-Petre/dosher)')
# ---- Contact----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    #Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/claudiu.gpetre@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_pic2, height=300, key="contact")
