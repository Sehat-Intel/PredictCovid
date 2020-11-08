import streamlit as st


import src.pages.tutorial as tutorial
import src.pages.signup as signup
import src.pages.dashboard as dashboard

import hash as hash

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['predict-covid']
collection = db['user-data']

st.set_page_config(
    page_title="Sehat Intel",
    page_icon="💊",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

st.title("Sehat Intel 💊")


menu = ["Tutorial","SignUp", "Login"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Tutorial":
    st.subheader("Tutorial")
    tutorial.main()

if choice == "SignUp":
    st.subheader("SignUp")
    signup.main()
    


if choice == "Login":
    st.sidebar.header("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        if email and password:
            obj = collection.find_one({"email": email})
            if obj:
                if (hash.check_hashes(password, obj['password'])):
                    st.info('Logged in as ' + obj['username'])
                    dashboard.main()
            else:
                st.warning('Invalid Username or Password, please try again')





st.subheader("""Covid-19 Detection using Deep Learning""" )
if st.sidebar.button('Like the app👍'):
    st.sidebar.text("Thank you 🥰")
    st.balloons()











if st.button("Show list of users"):
        st.write(list(collection.find()))




st.sidebar.markdown('![GitHub top language](https://img.shields.io/github/languages/top/tuminzee/PredictCovid?style=for-the-badge)  [![Github Repo](https://img.shields.io/badge/GitHub-Repo-green?style=for-the-badge&logo=appveyor)](https://github.com/tuminzee/PredictCovid)')
st.sidebar.markdown('![GitHub contributors](https://img.shields.io/github/contributors/tuminzee/PredictCovid?style=for-the-badge) ![GitHub forks](https://img.shields.io/github/forks/tuminzee/PredictCovid?label=Fork&style=for-the-badge)')
st.sidebar.markdown('![forthebadge](https://forthebadge.com/images/badges/for-you.svg) ![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)')



