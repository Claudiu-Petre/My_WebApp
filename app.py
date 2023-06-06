import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon="👾", layout="wide")

def load_lottieurl(url):
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
lottie_pic = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_7X0d6AzODk.json")
img_1 = Image.open("Images/cruise.png")
img_2 = Image.open("Images/mapper.png")


# ----HEADER-----
with st.container():
    st.subheader("Hi, my name is Claudiu 🖐")
    st.title("Junior Software Engineer from Leeds, UK 🇬🇧")
    st.subheader("JAVASCRIPT, REACT, EXPRESS, HTML, CSS, PYTHON")
    st.write("I am passionate about programming and amazed about how a few lines of code can change your life...and others 😂 ")
    st.write("[Learn more >](https://github.com/Claudiu-Petre)")
    st.markdown("")

# ----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(""" I am transitioning from Site managing into software development through a variety of: 
    - courses,
    - tutorials,
    - boot camps, 
    - books,
    -  etc. 

    Also, looking for opportunities that would allow me full time software development experience for a better and more versatile understanding of programming.
        """)

    with right_column:
        st_lottie(lottie_pic, height=600, key="coding")

# --- Projects---

with st.container():
    st.write("---")
    st.header("My Projects")
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
        st.empty()