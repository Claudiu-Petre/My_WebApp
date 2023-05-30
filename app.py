import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon="👾", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load assets---
lottie_pic = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_7X0d6AzODk.json")

# ----HEADER-----
with st.container():
    st.subheader("Hi, my name is Claudiu 🖐")
    st.title("Junior Software Engineer from Leeds, UK 🇬🇧")
    st.subheader(                     "JAVASCRIPT, REACT, EXPRESS, HTML, CSS, PYTHON")
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
        - books, etc. 

    Also, looking for opportunities that would allow me full time software development experience for a better and more versatile understanding of programming.
        """)

with right_column:
    st_lottie(lottie_pic, height=600, key="coding")