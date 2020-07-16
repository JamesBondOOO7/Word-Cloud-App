import streamlit as st
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

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


def main():
    st.sidebar.title("🌟 Select your favourite Image 🌟")

    img = st.sidebar.selectbox("Mask Images for Word Cloud",("CLOUD","INDIA","SPY","STAR","UPVOTE","LEAF","BIRD"))

    st.sidebar.header("Preview")
    img1 = Image.open("./Images/cloud.png")
    image = img1
    st.sidebar.image(img1, width=250, caption="CLOUD")

    img2 = Image.open("./Images/india.png")
    st.sidebar.image(img2, width=250, caption="INDIA")

    img3 = Image.open("./Images/spy.png")
    st.sidebar.image(img3, width=250, caption="SPY")

    img4 = Image.open("./Images/star.png")
    st.sidebar.image(img4, width=250, caption="STAR")

    img5 = Image.open("./Images/upvote.png")
    st.sidebar.image(img5, width=250, caption="UPVOTE")

    img6 = Image.open("./Images/leaf.png")
    st.sidebar.image(img6, width=250, caption="LEAF")

    img7 = Image.open("./Images/bird.png")
    st.sidebar.image(img7, width=250, caption="BIRD")

    if img == "INDIA":
        image = img2

    elif img == "SPY":
        image = img3

    elif img == "STAR":
        image = img4

    elif img == "UPVOTE":
        image = img5

    elif img == "LEAF":
        image = img6

    elif img == "BIRD":
        image = img7

    else:
        image = img1

    st.header("Select Background Color")
    bgc = st.radio("Background Color", ("White","Black","Yellow","Red","Blue","Green","Orange","Violet"), key="bgc")

    st.header("Select Maximim Number of Words")
    max_words = st.slider("Max Words" , 1000, 3000 , key="max_words")

    st.header("Set Width and Height")
    width = st.slider("Width" , 10, 50 , key="width")
    height = st.slider("Height" , 10, 60 , key="height")

    msg = st.text_area("Enter the Text","Type Here...")

    if st.button("Submit",key="b1"):
        draw_wordcloud(bgc, max_words, image, width, height, msg)



if __name__ == '__main__':
    main()
