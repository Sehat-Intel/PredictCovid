import streamlit as st

import src.pages.home as home
import src.pages.uploadImage as uploadImage
import src.pages.url as url
import src.pages.about as about

st.beta_set_page_config(
    page_title="Predict Covid",
    page_icon="💊",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

st.sidebar.title("Navigate Here")
nav = st.sidebar.radio("Select your options",["Home","Upload X-ray and Predict","X-ray Url and Predict", "About"])


#-------------------------------------------------------

if nav == "Home":
    home.main()

#-------------------------------------------------------

if nav == "Upload X-ray and Predict":
    uploadImage.main()

#--------------------------------------------------------

if nav == "X-ray Url and Predict":
    url.main()

#--------------------------------------------------------
if nav == "About":
    about.main()
