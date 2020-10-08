import streamlit as st

import src.pages.uploadImage as uploadImage
import src.pages.url as url
import src.pages.about as about
import src.pages.home as home

st.beta_set_page_config(
    page_title="Predict Covid",
    page_icon="💊",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

st.title("Predict Covid 💊")
st.subheader("""Detect the probablity of Covid-19 using Deep Learning""" )


nav = st.selectbox("Navigate to",["Home","Upload X-ray and Predict","X-ray Url and Predict", "About"], key=0)

if nav == "Home":
    home.main()

if nav == "Upload X-ray and Predict":
    uploadImage.main()

if nav == "X-ray Url and Predict":
    url.main()

if nav == "About":
    about.main()

if st.sidebar.button('Like the app👍'):
    st.sidebar.text("Thank you 🥰")
    st.balloons()
st.sidebar.markdown('![GitHub top language](https://img.shields.io/github/languages/top/tuminzee/Covid-19-Detection-using-Deep-Learning?style=for-the-badge)  [![Github Repo](https://img.shields.io/badge/GitHub-Repo-green?style=for-the-badge&logo=appveyor)](https://github.com/tuminzee/Covid-19-Detection-using-Deep-Learning)')
st.sidebar.markdown('![GitHub contributors](https://img.shields.io/github/contributors/tuminzee/Covid-19-Detection-using-Deep-Learning?style=for-the-badge) ![GitHub forks](https://img.shields.io/github/forks/tuminzee/Covid-19-Detection-using-Deep-Learning?label=Fork&style=for-the-badge)')
st.sidebar.markdown('![forthebadge](https://forthebadge.com/images/badges/for-you.svg) ![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)')


# Youtube vide link 
# [![forthebadge](https://forthebadge.com/images/badges/powered-by-electricity.svg)](https://forthebadge.com)