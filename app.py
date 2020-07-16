import streamlit as st
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

st.title("WORD CLOUD")

def draw_wordcloud(background_color, max_words, img, width, height, text):
    wc = WordCloud(
    background_color=background_color,
    max_words=max_words,
    stopwords = set(STOPWORDS),
    mask = np.array(img)
    )

    fig = plt.figure()
    wc.generate(text)
    fig.set_figwidth(width) # set width
    fig.set_figheight(height) # set height
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

def drawImg(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def main():
    st.sidebar.title("🌟 Select your favourite Image 🌟")

    img = st.sidebar.selectbox("Mask Images for Word Cloud",("CLOUD","INDIA","SPY","STAR","UPVOTE","LEAF","BIRD"))

    st.sidebar.header("Preview")

    p = Path("./Images/")

    data = {}
    dirs = p.glob("*")
    for file in dirs:
        Img = Image.open("./" + str(file))
        name = str(file).split('\\')[-1][:-4].upper()
        data[name] = Img
        st.sidebar.image(Img, width=250, caption=name)

    st.header("Select Background Color")
    bgc = st.radio("Background Color", ("White","Black","Yellow","Red","Blue","Green","Orange","Violet"), key="bgc")

    st.header("Select Maximim Number of Words")
    max_words = st.slider("Max Words" , 1000, 3000 , key="max_words")

    st.header("Set Width and Height")
    width = st.slider("Width" , 10, 50 , key="width")
    height = st.slider("Height" , 10, 60 , key="height")

    msg = st.text_area("Enter the Text","Type Here...")

    if st.button("Submit",key="b1"):
        draw_wordcloud(bgc, max_words, data[img], width, height, msg)
        

if __name__ == '__main__':
    main()
